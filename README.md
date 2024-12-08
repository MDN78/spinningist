## Test project. UI and API tests. Site 'Spinningist.ru'  
![image](assets/main_page.PNG)   
> A website for the sale of goods for fishermen and tourists.  
> [site SPINNINGIST.RU](https://spinningist.ru/)  

### Project used:  
<p  align="left">
<code><img width="5%" title="python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"></code>
<code><img width="5%" title="pytest" src="https://github.com/MDN78/MDN78/blob/main/assets/pytest.png"></code>
<code><img width="5%" title="jenkins" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg"></code>
<code><img width="5%" title="allure" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_report.png"></code>
<code><img width="5%" title="alluretestops" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_testops.png"></code>
<code><img width="5%" title="github" src="https://github.com/MDN78/MDN78/blob/main/assets/github.png"></code>  
<code><img width="5%" title="telegram" src="assets/tg.png"></code>   
<code><img width="5%" title="pycharm" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg"></code>  

---- 


#### Checks list:  
##### UI tests  
- [x] authorization registered user
- [x] authorization unregistered user  
- [x] test delivery manu
- [x] test payment menu
- [x] select spinning  
- [x] add spinning to cart
- [x] create order  

##### API tests  
---- 

### <img width="3%" title="pc" src="assets/pc.jpg"> Local start UI and API tests  
1) Download project and open in IDE
2) Create file `.env` and add dates for tests. Examples dates in file `.env.examples`
3) Execute command:

```commandline
pytest 
```  
4) Execute the requests to generate allure report.  
   note: command for Windows

```commandline
allure serve
```  

### <img width="3%" title="Allure" src="assets/allure_report.png"> Allure report  
Special detail report with all steps, screenshots, logs.  



### <img width="3%" title="Telegramm" src="assets/tg.png"> Получение уведомлений о прохождении тестов в Telegram  
Special report about tests in Telegramm.  