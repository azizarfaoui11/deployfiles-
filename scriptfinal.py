import argparse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select

def main(url, stock_title, product_name, category, quantity, price):
    # Crée une nouvelle instance du driver Chrome
    driver = webdriver.Chrome()

    try:
        # Accéder à la page d'accueil
        driver.get(url)

        # Ajouter une nouvelle catégorie
        # Attendre que le bouton "+" soit cliquable et cliquer dessus
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='+'][@class='btn btn-info']"))).click()
        
        # Remplir le titre de la catégorie
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "title"))
        )
        input_element.send_keys(stock_title)

        # Soumettre le formulaire pour ajouter la catégorie
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn btn-info')]")
        submit_button.click()
        print(f"Catégorie ajoutée : {stock_title}")
        # Attendez que l'élément d'une catégorie ajoutée apparaisse ou que la page se soit chargée
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '" + stock_title + "')]")))

        time.sleep(7)  # Attendre un peu pour permettre le traitement

        # Cliquer sur le bouton Détails pour accéder au produit
        #details_button = WebDriverWait(driver, 10).until(
        #   EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'btn btn-primary') and contains(text(),'Details')]"))
        #)
        details_button = driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-primary') and contains(text(),'Details')]")
        details_button.click()

        time.sleep(5)  # Attendre la redirection à la page de détails
        print("Accès à la page du produit.")

        # Ajouter un produit
        add_product_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@title='Add Item']"))
        )
        add_product_button.click()

        # Remplir le formulaire d'ajout de produit
        product_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "productName"))
        )
        product_name_input.send_keys(product_name)

        # Sélectionner la catégorie par son texte
        category_select = Select(driver.find_element(By.ID, "category"))
        category_select.select_by_visible_text(category)  # Sélectionner la catégorie entrée par l'utilisateur        

        # Remplir les autres champs
        quantity_input = driver.find_element(By.ID, "quantity")
        quantity_input.send_keys(quantity)

        price_input = driver.find_element(By.ID, "price")
        price_input.send_keys(price)

        # Cliquer pour ajouter le produit
        add_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary') and contains(text(),'Add')]")
        add_button.click()
        print(f"Produit ajouté : {product_name}")

        time.sleep(10)  # Attendre que le produit soit ajouté

        # Retour à la page d'accueil
        driver.get(url)
        print("Retour à la page d'accueil.")
        
        time.sleep(10)  # Temps pour voir le retour avant de fermer

    finally:
        # Ferme le navigateur
        driver.quit()

if __name__ == "__main__":
    # Définition des arguments à l'aide d'argparse
    parser = argparse.ArgumentParser(description='Script Selenium pour ajouter une catégorie et un produit')
    parser.add_argument('--url', type=str, required=True, help='URL de la page d\'accueil')
    parser.add_argument('--stock-title', type=str, required=True, help='Titre de la catégorie à ajouter')
    parser.add_argument('--product-name', type=str, required=True, help='Nom du produit à ajouter')
    parser.add_argument('--category', type=str, required=True, help='Catégorie du produit à ajouter (vous pouvez entrer n\'importe quelle catégorie)')
    parser.add_argument('--quantity', type=str, required=True, help='Quantité du produit à ajouter')
    parser.add_argument('--price', type=str, required=True, help='Prix du produit à ajouter')
    args = parser.parse_args()

    # Appel de la fonction principale avec les arguments fournis
    main(args.url, args.stock_title, args.product_name, args.category, args.quantity, args.price)