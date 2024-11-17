## Test project. UI and API tests. Site 'Spinningist.ru'  
![image](assets/main_page.PNG)   
> A website for the sale of goods for fishermen and tourists.  
> [site SPINNINGIST](https://spinningist.ru/)  

#### Checks list:  
##### UI tests  
- [x] authorization registered user
- [x] authorization unregistered user  
- [x] test main page  
- [x] select spinning  
- [x] add spinning to cart
- [x] create order  
- [x] authorization unregistered user

##### API tests  
---- 

### <img width="3%" title="pc" src="assets/pc.jpg"> Local start UI and API tests  
1) Download project and open in IDE
2) Create file `.env` and add dates for tests. Examples in file `.env.examples`
3) Execute command:

```commandline
pytest 
```  
4) Execute the requests to generate allure report.  
   note: command for Windows

```commandline
allure serve
```  