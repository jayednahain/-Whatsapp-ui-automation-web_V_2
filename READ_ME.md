# CASE ONE (TC-001)
1. go to whatsapp web
2. scan QR code manually
3. read number from excel
4. search number from search field
>* connected to web driver
>* Load CSV file with python using python pandas Library
>* Using for loop According to dataset length
>* "element" variable defines the number search box
>* using "send_key" sending each number on the search box 
>* lately using "clear" to clean the search box for sending another number
---


# CASE TWO (TC-002)
1. go to whatsapp web
2. scan QR code manually
3. read number from excel
4. search number
5. write message
6. send message

>* connected to web driver
>* Load CSV file with python using python pandas Library
>* Using for loop According to dataset length
>* "element" variable defines the number search box
>* using "send_key" sending each number on the search box 
>>>* using "send_data_box" targetting the massage typing box
>>>* "button" used to assign the button class
>>>* sending data using click function
>* lately using "clear" to clean the search box for sending another number
---

# CASE THREE (TC-003)
1. go to whatsapp web
2. scan QR code manually
3. read number from excel
4. search number
5. write message
6. send message 
7. write ""sent"" in excel for successful message sent

>* connected to web driver
>* Load CSV file with python using python pandas Library
>* Using for loop According to dataset length
>* "element" variable defines the number search box
>* using "send_key" sending each number on the search box 
>* using "send_data_box" targetting the massage typing box
>* "button" used to assign the button class
>>>* sending data using click function
>>>* after sending the data, update xlsx file asine 'sent' on  "delivery report" column
>* lately using "clear" to clean the search box for sending another number
---
# CASE FOUR (TC-004)
7.check seen/not seen status
8. write ""seen/not seen""  in excel
>* connected to web driver
>* Load CSV file with python using python pandas Library
>* Using for loop According to dataset length
>* "element" variable defines the number search box
>* using "send_key" sending each number on the search box 
>* using "send_data_box" targetting the massage typing box
>* "button" used to assign the button class
>* sending data using click function
>>>* "checK_xpath_unread" and "checK_xpath_unread " carries the list of reading massage and undread massage
>>>* Applying condition if the 'checK_xpath_unread' list value is 0, 'seen' will assign on 'status' column otherwise, 'unseen' will assign.
>>>* after updating the value of the column, exporting the 'new_data' Dataframe as '.xlsx' format 
>* lately using "clear" to clean the search box for sending another number
---

# CASE FOUR (TC-004)
1. go to whatsapp web
2. scan QR code manually
3. go to options menu (three vertical dot)
4. click logout

>* using 'dot' variable grabbing the drop-down class value
>* "log out" defines the log out class form drop down menu
>* uisng click funtion on "log out" will log out from whatsapp application


