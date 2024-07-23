from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import sys

# Vérifiez si l'URL est passée comme argument
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

# Récupère l'URL depuis l'argument de ligne de commande
url = sys.argv[1]

# Crée une nouvelle instance du driver Chrome
driver = webdriver.Chrome()

try:
    # Navigue vers le site web
    driver.get(url)

    # Récupère le titre de la page
    actual_title = driver.title
    print("Le titre est :", actual_title)

    # Récupère l'URL actuelle
    current_url = driver.current_url
    print("L'URL actuelle est :", current_url)

    # Fonction pour récupérer le texte d'un élément par son ID
    def get_element_text_by_id(element_id):
        try:
            element = driver.find_element("id", element_id)
            if element:
                return element.text
            else:
                return None
        except NoSuchElementException:
            return None

    # Fonction pour récupérer l'attribut d'un élément par sa classe
    def get_element_attribute_by_class(class_name, attribute_name):
        try:
            element = driver.find_element("class name", class_name)
            if element:
                return element.get_attribute(attribute_name)
            else:
                return None
        except NoSuchElementException:
            return None

    # Exemples d'utilisation des fonctions définies
    # Modifiez "header-id" et "example-link-class" par les valeurs appropriées selon votre application
    header_text = get_element_text_by_id("userDropdown")  # Par exemple, l'ID de l'élément dropdown utilisateur
    if header_text:
        print("Le texte de l'élément avec l'ID 'userDropdown' est :", header_text)
    else:
        print("L'élément avec l'ID 'userDropdown' n'a pas été trouvé.")

    link_href = get_element_attribute_by_class("nav-link", "href")  # Par exemple, la classe des liens de navigation
    if link_href:
        print("L'attribut 'href' du lien avec la classe 'nav-link' est :", link_href)
    else:
        print("Le lien avec la classe 'nav-link' n'a pas été trouvé.")

finally:
    # Ferme le navigateur
    driver.quit()
