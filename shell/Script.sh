read -p "Enter the password to replace:" newPassword 			#read the password from user
oldPassword=$(grep "password" db.config|awk -F":" '{print $2}') 		#read the old password from file depends on file format 
sed -ie "/password/ s/$oldPassword/$newPassword/" db.config		#replace old password with new depends on file format  
