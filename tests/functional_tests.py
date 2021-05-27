from selenium import webdriver

# Step 1. Test if Django is installed
browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert "Django" in browser.title
