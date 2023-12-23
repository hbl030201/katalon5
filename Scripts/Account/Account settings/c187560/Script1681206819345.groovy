import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('https://creativeboard.optoma.com/signin')

WebUI.maximizeWindow(FailureHandling.STOP_ON_FAILURE)

WebUI.setText(findTestObject('Sign in and out/Sign in page_email input'), 'creativeboard.at@gmail.com')

WebUI.setEncryptedText(findTestObject('Sign in and out/Sign in page_PW input'), 'gMOrSXrdjKGRQzi/ZJkP2Q==')

WebUI.click(findTestObject('Sign in and out/Sign in btn'))

WebUI.click(findTestObject('Sign in and out/myAccount'))

WebUI.click(findTestObject('Sign in and out/Account_Account settings'))

'先確認原本名字是"AT"'
WebUI.verifyElementText(findTestObject('Accounts/Account settings Name/Account settings_Name'), 'AT')

WebUI.click(findTestObject('Accounts/Account settings Name/Account settings_Name_edit btn'))

'更改名字為"123"'
WebUI.setText(findTestObject('Accounts/Account settings Name/Account settings_Name_edit_name input'), '123')

WebUI.click(findTestObject('Accounts/Account settings Name/Account settings_Name_edit_change btn'))

WebUI.click(findTestObject('Accounts/Account settings Name/Account settings_Name_edit_change_Ok btn'))

'確認更改後的名字是"123"'
WebUI.verifyElementText(findTestObject('Accounts/Account settings Name/Account settings_Name'), '123')

WebUI.closeBrowser()

