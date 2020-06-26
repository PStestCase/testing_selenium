import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.Test;

public class LoginUsingSelenium {

    @Test
    public void login() {
        WebDriver driver=new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://nj.myaccountqa.pseg.com/user/login");
        
        WebElement username=driver.findElement(By.id("username"));
        WebElement password=driver.findElement(By.id("password"));
        WebElement login = driver.findElement(By.id("submit"));

        username.sendKeys("andreww52");
        password.sendKeys("test1234");
        login.click();
    }
}