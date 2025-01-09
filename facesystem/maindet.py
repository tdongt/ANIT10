from PySide6.QtWidgets import QApplication,QWidget,QFileDialog
from systemmain_ui import Ui_Form
from reg_ui import Ui_Form as ui2
import cv2 as cv
import os
import urllib
import urllib.request
from PIL import Image
import numpy as np
from PySide6.QtCore import Signal,QTimer
from PySide6.QtGui import QImage, QPixmap,QPalette, QBrush
from pymysql import Connection
from gue_ui import Ui_Form as ui3
from untitled_ui import Ui_Form as ui4
from go_ui import Ui_Form as ui5
import requests
from urllib import parse
#主窗口类
class mainwin(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.facedetect.clicked.connect(self.detect)
        self.guestreg.clicked.connect(self.guestre)
        self.manager.clicked.connect(self.mana)
        #创建子窗口(访客登记类)对象
        self.guestman=guest()
        #创建子窗口(管理员界面)对象
        self.mang=maneger()
        #创建 QLabel 并设置默认图片
        self.default_pixmap = QPixmap('R.png')  # 替换为你的默认图片路径
        self.label.setPixmap(self.default_pixmap)
        self.label.setScaledContents(True)  # 让图片适应 QLabel 的大小
        #数据训练
        self.path='C:/Users/11299/Desktop/other/try/face_exec' #存放录入的照片集
        self.faces=[]
        self.ids=[]
        self.symb=0
        self.idp=None
        self.namep=None
        self.sexp=None
        self.sym2=0
        #警告时间定义
        self.warntime=0
        #通过时间定义
        self.yestime=0
        #管理员登录信号
        self.goo=manago()
        self.goo.data_subm.connect(self.accp)
        #加载识别器
        self.recognizer=cv.face.LBPHFaceRecognizer_create()
        self.recognizer.read('trainer/trainer.yml')
        self.reco2=cv.face.LBPHFaceRecognizer_create()
        self.reco2.read('trainer/trainer.yml')
        #连接数据库
        self.conp=Connection(
            host="localhost",
            port=3306,
            user="root",
            password="dong1129",
            autocommit=True
        )
        self.conp.select_db("faceinfo")
        #为窗口设置背景
        palette=self.palette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("C:/Users/11299/Pictures/222.jpg")))
        self.setPalette(palette)
        self.image_label = self.label
    #图像格式转换，使得图像显示在qlabel上
    def convert_cv_to_qt(self, img):
        """将 OpenCV 图像转换为 QImage,再转换为 QPixmap"""
        # OpenCV 图像是 BGR 格式，需要转换为 RGB
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        height, width, channels = img_rgb.shape
        bytes_per_line = channels * width
        q_img = QImage(img_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(q_img)
    #人脸检测函数
    def face_detect(self,img):
        #从数据库中得到和id对应姓名列表
        cursor=self.conp.cursor()
        cursor.execute("select name from namelist")
        data=cursor.fetchall()
        name_list=[]
        for row in data:
            rown=list(row)
            name_list.extend(rown)
        self.names=name_list
        #灰度转换
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        #调用分类器
        face_detect=cv.CascadeClassifier('C:/Users/11299/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
        face=face_detect.detectMultiScale(gray,1.1,5,0,(70,70),(300,300))
        for x,y,w,h in face:
            cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
            ids,confidence=self.recognizer.predict(gray[y:y+h,x:x+w])
            self.warningeditt.setText('请看向摄像头!')
            if confidence>90:
                self.warntime+=1
                if self.warntime>=50:
                    import winsound
                    #(频率,时长)
                    winsound.Beep(1000,100)
                    self.warningeditt.setText('未识别到您的人脸,非社区业主请进行访客登记')
                cv.putText(img,'unkonw',(x+10,y-20),cv.FONT_HERSHEY_SIMPLEX,0.75,(0,255,0),1)
            else:
                    #print(self.ids[])
                    #print(self.names[ids-1])
                cv.putText(img,str(self.names[ids-1]),(x+10,y-20),cv.FONT_HERSHEY_SIMPLEX,0.75,(0,255,0),1)
                self.yestime+=1
                if self.yestime>=25:
                    self.warningeditt.setText('识别到人脸,请尽快通过!')
        #cv.imshow('result',img)
         # 更新 QLabel 中显示的图像
        qt_img = self.convert_cv_to_qt(img)
        self.image_label.setPixmap(qt_img)
        self.image_label.setScaledContents(True)  # 确保图像适应 QLabel 尺寸
    #打开摄像头进行检测,调用人脸检测函数
    def detect(self):
        cap=cv.VideoCapture(0,cv.CAP_DSHOW)
        cap.read()
        while True:
            self.flag,self.frame =cap.read()
            if not self.flag:
                break
            self.face_detect(self.frame)
            if ord('q')==cv.waitKey(24):
                 break
        cv.destroyAllWindows()
    def accp(self,sym):
        self.sym2=sym
        print(f"接受到登录信号{self.sym2}")
    #打开管理员界面
    def mana(self):
        if self.sym2==0:
            self.goo.show()
        else:
            self.mang.show()
    def guestre(self):
        self.guestman.show()




#子窗口访客登记界面
class guest(QWidget,ui3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.guesths)
        #连接数据库
        self.cons=Connection(
            host="localhost",
            port=3306,
            user="root",
            password="dong1129",
            autocommit=True
        )
        self.cons.select_db("faceinfo")
        palette=self.palette()
        #设置窗口背景
        palette.setBrush(QPalette.Window, QBrush(QPixmap("C:/Users/11299/Pictures/222.jpg")))
        self.setPalette(palette)
    def guesths(self):
        print("调用guest")
        nameg=self.lineEditname.text()
        sexg=self.lineEditsex.text()
        reasong=self.textEdit.toPlainText()
        dateg=self.lineEditdate.text()
        timeg=self.lineEdittme.text()
        #将访客信息存入访客登记表
        try:
            cursor = self.cons.cursor()
            cursor.execute("INSERT INTO guest (name,sex,reason,todate,totime) VALUES (%s,%s,%s, %s, %s)", ({nameg},{sexg},{reasong},{dateg},{timeg}))
        except Exception as e:
            print(f"Error: {e}")
        self.close()
#管理员登录界面
class manago(QWidget,ui5):
    #自定义信号，当账号密码正确，向主界面发送信号，进入管理员界面
    data_subm=Signal(int)
    def __init__(self,parent=None):
        super().__init__()
        parent=mainwin
        self.setupUi(self)
        self.mana=maneger()
        self.pushButton.clicked.connect(self.gogo)
        palette=self.palette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("C:/Users/11299/Pictures/222.jpg")))
        self.setPalette(palette)
    def gogo(self):
        Account=self.lineEdit.text()
        password=self.lineEdit_2.text()
        #code=self.lineEdityan.text()
        if Account=='1129':
            print("账号正确")
            if password=='dong':
                print("密码正确")
                
                sym=1
                self.data_subm.emit(sym)
                self.mana.show()
                self.close()
            else:
                self.lineEdit_3.setText('密码错误')
        else:
            self.lineEdit_3.setText('账号错误')
    def yanz(self):
        pass
#管理员界面
class maneger(QWidget,ui4):
    def __init__(self,parent=None):
        super().__init__()
        self.setupUi(self)
        #设置背景
        palette=self.palette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap("C:/Users/11299/Pictures/222.jpg")))
        self.setPalette(palette)
        self.parent=manago
        #数据训练
        self.path='C:/Users/11299/Desktop/other/try/face_exec'
        #定义注册框对象
        self.reg=registerwin()
        self.symb=0
        self.idp=None
        self.namep=None
        self.sexp=None
        self.reg.data_submitted.connect(self.accepths)
        #下拉框内容
        self.options=['全部','日期','时间','姓名','性别']
        self.comboBox.addItems(self.options)
        #按钮信号绑定
        self.faceget.clicked.connect(self.getface)
        self.facetrain.clicked.connect(self.bind)
        self.guestcheck.clicked.connect(self.check)
        self.picture.clicked.connect(self.picdetect)
        self.hostcheck.clicked.connect(self.hcheck)
        #连接数据库
        self.conn=Connection(
            host="localhost",
            port=3306,
            user="root",
            password="dong1129",
            autocommit=True
        )
        self.conn.select_db("faceinfo")
        self.reco2=cv.face.LBPHFaceRecognizer_create()
        self.reco2.read('trainer/trainer.yml')
    def accepths(self,symx,idx,namex,sexx):
        print(f"收到注册数据: 注册标志{symx}, ID={idx}, Name={namex}, Sex={sexx}")
        self.symb=symx
        self.idp=idx
        self.namep=namex
        self.sexp=sexx
        #window.names.append(namex)
        #将姓名，id信息存入namelist表 人脸识别时会从namelist表中通过id和name按序进行人脸匹配
        cursor=self.conn.cursor()
        cursor.execute("INSERT INTO namelist (id,name) VALUES (%s, %s)", ({self.idp},{self.namep}))
        #cursor.close()
    def bind(self):
        self.faces,self.ids=self.execise()
        self.recog=cv.face.LBPHFaceRecognizer_create()
        self.recog.train(self.faces,np.array(self.ids))
        #将训练后生成的人脸信息向量存入训练数据
        self.recog.write('trainer/trainer.yml')
    #训练指定路径下的图像集并存储
    def execise(self):
        #存储人脸数据
        facedatas=[]
        #存储姓名数据
        ids=[]
        #存储图片信息
        imagepaths=[os.path.join(self.path,f) for f in os.listdir(self.path)]
        #加载分类器
        face_detecter=cv.CascadeClassifier('C:/Users/11299/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
        for imagepath in imagepaths:
        #打开图片，灰度化
            PIL_img=Image.open(imagepath).convert('L')
        #将图像转换为数组，以黑白深浅存储
            img_numpy=np.array(PIL_img,'uint8')
        #获取人脸特征
            faces=face_detecter.detectMultiScale(img_numpy)
        #获取每张图片的id和对应姓名
            id =int(os.path.split(imagepath)[1].split('.')[0])
            for x,y,w,h in faces:
                ids.append(id)
                facedatas.append(img_numpy[y:y+h,x:x+w])
        print(ids)
        print('id',id)
        print('fs',facedatas)
        return facedatas,ids
    def getface(self):
        if self.symb==0:
            self.reg.show()
        #self.symb,self.idp,self.namep,self.sexp=self.reg.register()
        #print("获取成功")
        else:
            print(f"getface的标志{self.symb}")
            cap=cv.VideoCapture(0,cv.CAP_DSHOW)
            flag=1
            num=1
            while(cap.isOpened()):
                ret_flag,Vshow =cap.read() #得到图像
                cv.imshow("capture",Vshow) #显示图像
                k=cv.waitKey(24) & 0xFF  #按键判断
                if k==ord('s'):
                    cv.imwrite("C:/Users/11299/Desktop/other/try/face_exec/"+self.idp+"."+self.namep+"."+str(num)+".jpg",Vshow)
                    print("成功检测检测并保存"+str(num)+".jpg")
                    print("--------------")
                    num+=1
                elif k==ord(' '):
                    break
            else:
                print("未录入信息,失败")
        #释放摄像头
        cap.release()
        cv.destroyAllWindows()
    #访客查询函数
    def check(self):
        cursor2=self.conn.cursor()
        item=self.comboBox.currentText()
        if item=='全部':
            cursor2.execute("select * from guest")
            data=cursor2.fetchall()
            #self.textEdityes.setText(str(data))
            self.textEdityes.clear()
            for row in data:
                self.textEdityes.append(str(row))
        elif item=='姓名':
            xname=self.chaxun.text()
            print(item)
            cursor2.execute("SELECT * FROM guest WHERE name = %s",(xname))
            data=cursor2.fetchall()
            self.textEdityes.clear()
            for row in data:
                self.textEdityes.append(str(row))
        elif item=='日期':
            xdate=self.chaxun.text()
            print(item)
            cursor2.execute("SELECT * FROM guest WHERE todate = %s",(xdate))
            data=cursor2.fetchall()
            self.textEdityes.clear()
            for row in data:
                self.textEdityes.append(str(row))
        elif item=='性别':
            xsex=self.chaxun.text()
            print(item)
            cursor2.execute("SELECT * FROM guest WHERE sex = %s",(xsex))
            data=cursor2.fetchall()
            self.textEdityes.clear()
            for row in data:
                self.textEdityes.append(str(row))
        elif item=='时间':
            xtime=self.chaxun.text()
            print(item)
            cursor2.execute("SELECT * FROM guest WHERE totime = %s",(xtime))
            data=cursor2.fetchall()
            self.textEdityes.clear()
            for row in data:
                self.textEdityes.append(str(row))
    #图片检测函数
    def picdetect(self):
        #选择图片
        pathh=QFileDialog.getOpenFileName(self,'打开一个图片','C:/Users/11299/Pictures','图片(*.img);;图片2(*.jpg)')[0]
        self.img=cv.imread(pathh)
        #imgx=cv.resize(img,dsize=(1000,1300))
        #检测函数
        self.face_detect()
    #图片检测主程序
    def face_detect(self):
        cursor3=self.conn.cursor()
        cursor3.execute("select name from namelist")
        data=cursor3.fetchall()
        name_list=[]
        for row in data:
            rown=list(row)
            #print(rown)
            name_list.extend(rown)
        self.namee=name_list
        #灰度转换
        gray=cv.cvtColor(self.img,cv.COLOR_BGR2GRAY)
       #调用分类器
        face_detect=cv.CascadeClassifier('C:/Users/11299/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')

        face=face_detect.detectMultiScale(gray)
        for x,y,w,h in face:
            cv.rectangle(self.img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
            ids,confidence=self.reco2.predict(gray[y:y+h,x:x+w])
            if confidence>90:
                   #global warntime
                   #warntime+=1
                cv.putText(self.img,'unkonw',(x+10,y-20),cv.FONT_HERSHEY_SIMPLEX,0.75,(0,255,0),1)
            else:
                    #print(self.ids[])
                    #print(self.names[ids-1])
                cv.putText(self.img,str(self.namee[ids-1]),(x+10,y-20),cv.FONT_HERSHEY_SIMPLEX,0.75,(0,255,0),1)
        cv.imshow('result',self.img)
    def hcheck(self):
        cursor3=self.conn.cursor()
        cursor3.execute("select * from reg")
        data=cursor3.fetchall()
        self.textEdityes.clear()
        for row in data:
            self.textEdityes.append(str(row))


#子窗口,注册框界面
class registerwin(QWidget,ui2):
    #自定义信号 传送业主注册信息 便于后续人脸信息保存
    data_submitted = Signal(int,str,str,str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.getreg)
        self.con=Connection(
            host="localhost",
            port=3306,
            user="root",
            password="dong1129",
            autocommit=True
        )
        self.con.select_db("faceinfo")
         #界面背景
        palette=self.palette()                       
        palette.setBrush(QPalette.Window, QBrush(QPixmap("C:/Users/11299/Pictures/222.jpg")))
        self.setPalette(palette)
    def getreg(self):
        self.register()
    def register(self):
        print("调用register")
        idx=self.lineEdit.text()
        namex=self.lineEdit_2.text()
        sexx=self.lineEdit_4.text()
        try:
            cursor = self.con.cursor()
            cursor.execute("INSERT INTO reg (id,name,sex) VALUES (%s, %s, %s)", ({idx},{namex},{sexx}))
            symx=1
            #self.con.close()
            print(f"注册数据:symbol={symx},id={idx},name={namex},sex={sexx}")
            self.data_submitted.emit(symx,idx,namex,sexx)
        except Exception as e:
            symx=0
            print(f"Error: {e}")
        #print(sym)
        self.close()
        return symx,idx,namex,sexx

if __name__ =='__main__':
    path='C:/Users/11299/Desktop/other/try/face_exec'
    app=QApplication()
    window=mainwin()
    window.show()
    app.exec()