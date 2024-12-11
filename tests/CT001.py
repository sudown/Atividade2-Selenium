from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração do WebDriver usando WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Passo 1: Acessar a página de login
    driver.get('http://sga.leiteviana.com:8080/')
    time.sleep(3)  # Aguarde 3 segundos para observar a página carregando

    # Passo 2: Clicar no link "Clique aqui para se cadastrar"
    link_cadastro = driver.find_element(By.LINK_TEXT, "Clique aqui para se cadastrar")
    time.sleep(2)  # Aguarde 2 segundos antes de clicar
    link_cadastro.click()
    time.sleep(3)  # Aguarde 3 segundos para observar a transição

    # Passo 3: Preencher os campos de cadastro
    campo_email = driver.find_element(By.ID, "email")
    campo_email.send_keys("teste@email.com")
    time.sleep(2)  # Aguarde 2 segundos

    campo_user = driver.find_element(By.ID, "user")
    campo_user.send_keys("usuarioTeste")
    time.sleep(2)  # Aguarde 2 segundos

    campo_senha = driver.find_element(By.ID, "senha")
    campo_senha.send_keys("senhaSegura123")
    time.sleep(2)  # Aguarde 2 segundos

    # Passo 4: Clicar no botão "Cadastrar"
    botao_cadastrar = driver.find_element(By.XPATH, "//button[text()='Cadastrar']")
    time.sleep(2)  # Aguarde 2 segundos antes de clicar
    botao_cadastrar.click()

    # Pausa para observar o comportamento após enviar o formulário
    time.sleep(5)

finally:
    # Fechar o navegador após o teste
    driver.quit()
