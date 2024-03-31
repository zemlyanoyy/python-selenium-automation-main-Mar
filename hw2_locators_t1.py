# Amazon Logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")


# Email Field
driver.find_element(By.ID, "ap_email")


# Continue button
driver.find_element(By.ID, "continue")


# Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href,'Id=508088')]")


# Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href,'Id=468496')]")


# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")


# Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')


# Other issues with Sign-in link
driver.find_element(By.ID, 'ap-other-signin-issues-link')


# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')
