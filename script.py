import argparse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def main(url, element_id, class_name):
    # Crée une nouvelle instance du driver Chrome
    driver = webdriver.Chrome()

    try:
        # Navigue vers le site web spécifié
        driver.get(url)

        # Récupère le titre de la page
        actual_title = driver.title
        print("Le titre est :", actual_title)

        # Récupère l'URL actuelle
        current_url = driver.current_url
        print("L'URL actuelle est :", current_url)

        # Fonction pour récupérer le texte d'un élément par son ID avec attente
        def get_element_text_by_id(element_id):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, element_id))
                )
                return element.text
            except (NoSuchElementException, TimeoutException):
                return None

        # Fonction pour récupérer l'attribut d'un élément par sa classe avec attente
        def get_element_attribute_by_class(class_name, attribute_name):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, class_name))
                )
                return element.get_attribute(attribute_name)
            except (NoSuchElementException, TimeoutException):
                return None

        # Fonction pour cliquer sur un élément par sa classe avec attente
        def click_element_by_class(class_name):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, class_name))
                )
                element.click()
                return True
            except (NoSuchElementException, TimeoutException):
                return False

        # Exemples d'utilisation des fonctions définies
        header_text = get_element_text_by_id(element_id)
        if header_text:
            print(f"Le texte de l'élément avec l'ID '{element_id}' est :", header_text)
        else:
            print(f"L'élément avec l'ID '{element_id}' n'a pas été trouvé.")

        link_href = get_element_attribute_by_class(class_name, "href")
        if link_href:
            print(f"L'attribut 'href' du lien avec la classe '{class_name}' est :", link_href)
        else:
            print(f"Le lien avec la classe '{class_name}' n'a pas été trouvé.")

        # Clique sur le lien et vérifie la redirection
        if click_element_by_class(class_name):
            # Attends que la redirection se produise
            WebDriverWait(driver, 10).until(EC.url_contains("/pipeline"))
            new_url = driver.current_url
            if "/pipeline" in new_url:
                print("Redirection réussie vers :", new_url)
            else:
                print("Redirection échouée. URL actuelle :", new_url)
        else:
            print(f"Le lien avec la classe '{class_name}' n'a pas pu être cliqué.")

        # Ajoute une pause de 10 secondes avant de fermer le navigateur
        time.sleep(10)

    finally:
        # Ferme le navigateur
        driver.quit()

if __name__ == "__main__":
    # Définition des arguments à l'aide d'argparse
    parser = argparse.ArgumentParser(description='Script Selenium avec paramètres')
    parser.add_argument('--url', type=str, required=True, help='URL du site web à visiter')
    parser.add_argument('--element-id', type=str, required=True, help="ID de l'élément pour récupérer le texte")
    parser.add_argument('--class-name', type=str, required=True, help="Classe de l'élément pour récupérer l'attribut")
    args = parser.parse_args()

    # Appel de la fonction principale avec les arguments fournis
    main(args.url, args.element_id, args.class_name)
