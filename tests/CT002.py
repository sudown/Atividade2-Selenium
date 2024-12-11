from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def login():
    # Configuração do WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Passo 1: Acessar a página principal do sistema
        driver.get("http://sga.leiteviana.com:8080/")  # Substitua pelo URL real da página
        
        # Aguarda o carregamento completo da página
        #time.sleep(2)

        # Passo 2: Informe o nome do usuário
        username_field = driver.find_element(By.ID, "user")
        username_field.send_keys("ocelot")  # Substitua pelo usuário válido
        #time.sleep(1)  # Pausa para visualização

        # Passo 3: Informe a senha do usuário
        password_field = driver.find_element(By.ID, "senha")
        password_field.send_keys("Oi@12345")  # Substitua pela senha válida
        #time.sleep(1)  # Pausa para visualização

        # Passo 4: Clicar no botão de Login
        login_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        login_button.click()

        # Aguarda o redirecionamento
        time.sleep(5)

        # Critério de êxito: Verificar se a tela principal foi carregada
        assert "Sistema de Gerenciamento de Alunos" in driver.page_source  # Substitua por texto único da página principal
        print("Teste CT002 – Sucesso: Login realizado com sucesso.")

    except AssertionError:
        print("Teste CT002 – Falha: Não foi possível acessar a tela principal do sistema.")
    except Exception as e:
        print(f"Erro durante o teste: {e}")
    finally:
        # Fecha o navegador
        driver.quit()

# Executa o teste
login()
