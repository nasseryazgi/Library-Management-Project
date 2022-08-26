Library management system 

The library management system is all about organizing, managing the library, and library-oriented tasks. It also involves maintaining the files of entering new books and the record of books that have been retrieved or issued, with their respective dates. 
نظام إدارة المكتبة هو كل شيء عن تنظيم وإدارة المكتبة والمهام الموجهة للمكتبة. كما يتضمن الاحتفاظ بملفات إدخال الكتب الجديدة وسجل الكتب التي تم استردادها أو إصدارها مع تواريخها.
The main aim of this project is to provide an easy to handle and automated library management system. This project also provides features and an interface for maintaining librarian’s records, User history of issues, and fines. The owner can easily update, delete and insert data in the files with this project.  
الهدف الرئيسي من هذا المشروع هو توفير نظام آلي لإدارة المكتبات سهل التعامل معه. يوفر هذا المشروع أيضًا ميزات وواجهة للحفاظ على سجلات أمين المكتبة وسجل المستخدم للمشكلات والغرامات. يمكن للمالك بسهولة تحديث وحذف وإدراج البيانات في الملفات باستخدام هذا المشروع

.
The library management has 2 types of users: 
1-	Admin 
2-	Users (students) 
Admin functions: 







Mange Books: 
1.	Adding Books:  
Add Book will provide utility to add the books and then store it in the file. This addition of books will take BookID, Name, Author and Edition as input.
خاصية إضافة اكتب وبعد الإضافة تخزينها في ملفات 
يوجد لها العديد من المتغيرات في الكلاس التي تتمثل في رقم خاص لكل كتاب واسم الكتاب وكاتب الكتاب وإصدار الكتاب   
2.	Issue Books: 
This is the core function of our management system as it issues the book to the student and records the return date. 
من خلالها يتم اصدار كتاب (يعني استعارة ) وبعد الاستعارة للطالب يتم عمل تاريخ ارجاع 
مثلاً ارجاع الكتاب بعد شهر 
3.	Update Book: 
authorize the admin to modify/update details of the book. 
من خلال هذه الخاصية بقدر اعمل تحديث ل بيانات الكتاب واللي بيقدر يعمل تحديث فقط المسؤال مش المستخدم  العادي ف ركز في هادي النقطة
4.	Return Books: 
In the return books function, students can return the book and they will be charged if it’s above due
سيتم ارجاع الكتاب واذا تأخر وقت الإرجاع يتم محاسبة الطالب .  
5.	Delete Books: 
Delete Books function will delete the inputted book ID from the Library 
سيتم حدف الكتاب حسب الرقم الخاص الذي سوف يتم إدخاله 
6.	Searching Books  :
function will look for the Book ID inputted and display the result if it’s available 
يتم البحث عن الكتب عن طريق الرقم الخاص بكل كتاب 
7.	Show Books: 
// add , update , issued ( show books)
Display all the books in the library 
هين بنعمل على اظهار جميع الكتب اللي بالمكتبة 
8.	show issued books 
Display all the issued books in the library 
اظهار جميع الكتب اللي تم استعارتها وطباعتها 



Admin 
Mange Users
العمليات اللي لازم المستخدم يقدر يعملهن
1-	Add new User 
2-	Display users
3-	 Delete user 
4-	 Update user. 
 
Student functions: 
1-	Search Book  
2-	View Issued Books Book attributes:  
Book-Name: 
The name of the book which is almost unique in some way. 
اسم الكتاب 
Book-Code: 

A number to use for sorting and arranging the book, as well as identifying it in the library. 
رقم يستخدم لفرز وترتيب الكتاب والتعرف عليه بالمكتبة.
Author: 
The one who has written the book. As sometimes the book’s series becomes more popular by the author’s name rather than the book name. 
اسم الشخص الذي كتب الكتاب 
Price: 
The market value of the book is also required to maintain in the record, as sometimes it is needed to arrange and sort based on this, secondly, it is also required for compensation in case of loss or damage, as fine charges. .
السعر الخاص بكل كتاب 
Quantity: 



This is to indicate the availability of each book individually, so as to know whether the last copy should be issued or kept as a reference piece. Also, to maintain the number of books. 
عدد الكتب المتوفرة من هذا الكتاب 
Rack-No: 
To get the exact location of the book, so as it becomes easy to search it and sort it at the time of binding up work. 
رقم خاص للتميز بين التخصصات المختلفة 
Subject-Code: 
As there are various further divisions and subcategories of any subject. So, in that case, this is the unique id to distinguish the books, arrange them, and sort them. Like in computer science there are further many more specialties like core java, advanced java, HTML, html5, etc. 


User attributes: 
The next is the beneficiary, by whom the library is being accessed, and who serves as a purpose for this system. 
Its attributes include: 
Name: 
The name of the student, who will get the book issued, or who will return the book.
اسم المستخدم 
Id: 
The user’s unique college or university roll number i.e. the id. The same is applicable to teachers also, with their unique id. 
الكود الخاص بكل مستخدم


Address: 
This refers to the user’s physical area of residence. It is a composite attribute. As it further contains the house number and lane number. 
العنوان الخاص بكل مستخدم
Issue Status: 
It makes to the notice of the librarian as well as to the student or teacher that ow many books they have already got issued and how much more can they get at the current point of time.  
الحالة الخاصة بإصدار الكتب عشان اضمن انو الكتاب راح يرجع وهيك
It includes attributes as: 
Book-Name: 
The name of the book which is almost unique in some way. .
اسم الكتاب 
Book-Code: 
A number to use for sorting and arranging the book, as well as identifying it in the library. 
رقم الكتاب 



Id: 
The user’s unique college or university roll number i.e. the id. The same is applicable to teachers also, with their unique id. To know which user has been issued the book and for what time limit, that is what time the user is supposed to return the book, and if not will be charged a fine. 
رقم الطالب الذي سوف يتم فرض عليه العقووبة 
Date-Issue: 
The date on which user got the book issued to read from it. 
الوقت الذي فيه على الكتاب 
Return-Date: 
It indicates the date on which the user is supposed to be returning the book, that is it is the date after the duration completed for which the user has been issued the book. 
الوقت الذي يذي يجب فيه ارجاع الكتاب .





 
Return Status: 
This tells the library management authority about the status of returned books per user. Whether a particular user has returned the book or not, on or before the last date. If not, in that case, the fine will be charged from him/her as a penalty for a late submission. 
هذا يخبر سلطة إدارة المكتبة عن حالة الكتب المرتجعة لكل مستخدم. ما إذا كان مستخدم معين قد أعاد الكتاب أم لا ، في التاريخ الأخير أو قبله. إذا لم يكن الأمر كذلك ، في هذه الحالة ، سيتم فرض الغرامة عليه / عليها كعقوبة للتقديم المتأخر.
Book-Name: 
The name of the book which is almost unique in some way.
اسم الكتاب 
Book-Code: 
A number to use for sorting and arranging the book, as well as identifying it in the library. 
رقم يستخدم
Id: 
The user’s unique college or university roll number i.e. the id. The same is applicable to teachers also, with their unique id. To know which user has been issued the book and for what time limit, that is what time the user is supposed to return the book, and if not will be charged a fine. 
رقم تسجيل الكلية
Date-Issue: 
The date on which user got the book issued to read from it. 
التاريخ الذي حصل فيه المستخدم على الكتاب للقراءة منه.
Return-Date: 
It indicates the date on which the user is supposed to be returning the book, that is it is the date after the duration completed for which the user has been issued the book. 
يشير إلى التاريخ الذي من المفترض أن يقوم فيه المستخدم بإعادة الكتاب ، أي التاريخ الذي يلي المدة التي تم فيها إصدار الكتاب للمستخدم.
 
•	The project should implement the concepts of OOP in python  
•	All books and users data should be kept and updated in files  
 




















Admin 
Add User 
Delete user
Update 
Display user

Admin 
1-	Add book 
2-	Delete 
3-	Issud 
4-	Update 
5-	Display 
6-	Retuen 
7-	

User 
1-	Seacr
2-	 View Issued 





