from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def buscar_aluno():
    # Configuração do WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Passo 1: Acessar a página inicial do sistema
        driver.get("http://sga.leiteviana.com:8080/index")

        # Passo 2: Clicar no botão "Pesquisar Aluno"
        pesquisar_aluno_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Pesquisar Aluno"))
        )
        pesquisar_aluno_button.click()

        # Passo 3: Verificar se a página de pesquisa foi carregada
        # ... (Verificar se algum elemento específico da página de pesquisa está presente)

        # Passo 4: Clicar em "Todos os Alunos Ativos no Sistema"
        alunos_ativos_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".card:first-child .btn"))
        )
        alunos_ativos_button.click()

        time.sleep(2)

        # Verify if the table is present
        try:
            # Using reliable CSS selector for the table
            alunos_tabela = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table.table.table-bordered.table-hover"))
            )
            print("Tabela de alunos encontrada!")
        except NoSuchElementException:
            print("Tabela de alunos NÃO encontrada!")

        time.sleep(2)

        pesquisar_aluno_button2 = WebDriverWait(driver, 10).until(
          EC.element_to_be_clickable((By.LINK_TEXT, "Pesquisar Aluno"))
        )
        pesquisar_aluno_button2.click()

        time.sleep(2)

        alunos_inativos_button = WebDriverWait(driver, 10).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, ".card:nth-child(2) .btn"))
        )
        alunos_inativos_button.click()

        # Verify if the table is present
        try:
            # Using reliable CSS selector for the table
            alunos_tabela = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table.table.table-bordered.table-hover"))
            )
            print("Tabela de alunos encontrada!")
        except NoSuchElementException:
            print("Tabela de alunos NÃO encontrada!")
            
        time.sleep(2)

        # ... (Verificar se a nova página foi carregada)

    finally:
        driver.quit()

# Executar o teste
buscar_aluno()