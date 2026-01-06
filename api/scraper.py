# # import requests
# # from bs4 import BeautifulSoup
# # import os
# # from urllib.parse import urljoin, urlparse
# # import time

# # def scrape_zt_hosting():
# #     base_url = "https://zthosting.com/"
# #     visited = set()  # Ye duplicates ko rokay ga
# #     to_visit = [base_url]
    
# #     # --- CONTROL SETTINGS ---
# #     MAX_PAGES = 100   # Sirf top 50 zaroori pages (itny kafi hain pure data ke liye)
# #     scraped_count = 0
    
# #     data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')
# #     if not os.path.exists(data_folder): os.makedirs(data_folder)

# #     print(f"🚀 Optimized Scraper started (Limit: {MAX_PAGES} pages)...")

# #     while to_visit and scraped_count < MAX_PAGES:
# #         current_url = to_visit.pop(0)
        
# #         # 1. Duplicate Check: Agar visited set mein hai to skip karo
# #         if current_url in visited or "#" in current_url:
# #             continue
            
# #         try:
# #             # User-Agent lagana zaroori hai taake website block na kare
# #             headers = {'User-Agent': 'Mozilla/5.0'}
# #             response = requests.get(current_url, headers=headers, timeout=10)
# #             visited.add(current_url)

# #             if response.status_code == 200:
# #                 soup = BeautifulSoup(response.text, 'html.parser')
                
# #                 # Page ka naam saaf karna (URL se file name banana)
# #                 path = urlparse(current_url).path.strip('/')
# #                 file_name = f"{path if path else 'zt_home_page'}.txt".replace('/', '_')
                
# #                 # Sirf Main content uthana (Header/Footer ki gandagi se bachne ke liye)
# #                 content = soup.find('main') or soup.find('article') or soup.body
# #                 if content:
# #                     text_data = content.get_text(separator='\n', strip=True)
                    
# #                     # File save karna
# #                     with open(os.path.join(data_folder, file_name), "w", encoding="utf-8") as f:
# #                         f.write(f"Source: {current_url}\n" + "="*30 + "\n" + text_data)
                    
# #                     scraped_count += 1
# #                     print(f"✅ {scraped_count}/{MAX_PAGES}: Updated {file_name}")

# #                 # 2. Smart Link Finding
# #                 for link in soup.find_all('a', href=True):
# #                     full_link = urljoin(base_url, link['href'])
                    
# #                     # Sirf ZT Hosting ke internal links ho aur media files na hon
# #                     if urlparse(full_link).netloc == urlparse(base_url).netloc:
# #                         # Be-fuzool links ko filter karna (Very Important)
# #                         junk_words = ['replytocom', '.jpg', '.png', '.pdf', '/tag/', '/category/', '/author/']
# #                         if not any(word in full_link for word in junk_words):
# #                             if full_link not in visited:
# #                                 to_visit.append(full_link)
            
# #             time.sleep(0.5) # Server ko thora rest dena

# #         except Exception as e:
# #             print(f"❌ Error scraping {current_url}: {e}")

# #     print(f"🏁 Done! Total {scraped_count} unique pages saved in /data folder.")

# # if __name__ == "__main__":
# #     scrape_zt_hosting()


# # Is code ko apne api/scraper.py mein replace kar dein. Maine ismein hashing daal di hai jo check karegi ke agar website pe waqayi koi change aya hai tabhi file overwrite ho.



# import requests
# from bs4 import BeautifulSoup
# import os
# from urllib.parse import urljoin, urlparse
# import time
# import hashlib # Naya: Content check karne ke liye

# def get_content_hash(text):
#     return hashlib.md5(text.encode('utf-8')).hexdigest()

# def scrape_zt_hosting():
#     base_url = "https://zthosting.com/"
#     visited = set()
#     to_visit = [base_url]
#     MAX_PAGES = 100
#     scraped_count = 0
#     any_file_updated = False # Flag to check if we need to sync DB

#     data_folder = os.path.join(os.path.dirname(__file__), '..', 'data', 'scraped_pages')
#     if not os.path.exists(data_folder): os.makedirs(data_folder)

#     print(f"🚀 Daily Sync Scraper started...")

#     while to_visit and scraped_count < MAX_PAGES:
#         current_url = to_visit.pop(0)
#         if current_url in visited or "#" in current_url: continue
            
#         try:
#             headers = {'User-Agent': 'Mozilla/5.0'}
#             response = requests.get(current_url, headers=headers, timeout=10)
#             visited.add(current_url)

#             if response.status_code == 200:
#                 soup = BeautifulSoup(response.text, 'html.parser')
#                 path = urlparse(current_url).path.strip('/')
#                 file_name = f"{path if path else 'zt_home_page'}.txt".replace('/', '_')
#                 file_path = os.path.join(data_folder, file_name)
                
#                 content = soup.find('main') or soup.find('article') or soup.body
#                 if content:
#                     text_data = content.get_text(separator='\n', strip=True)
#                     new_hash = get_content_hash(text_data)
                    
#                     # Check if update is needed
#                     should_write = True
#                     if os.path.exists(file_path):
#                         with open(file_path, "r", encoding="utf-8") as f:
#                             # Pehli line 'Source' hoti hai, hum sirf content check karenge
#                             old_content = f.read()
#                             if new_hash in old_content: # Simple hash check
#                                 should_write = False

#                     if should_write:
#                         with open(file_path, "w", encoding="utf-8") as f:
#                             f.write(f"Source: {current_url}\nHash: {new_hash}\n" + "="*30 + "\n" + text_data)
#                         any_file_updated = True
#                         print(f"✨ Updated: {file_name}")
                    
#                     scraped_count += 1

#                 # Link finding logic (Same as yours)
#                 for link in soup.find_all('a', href=True):
#                     full_link = urljoin(base_url, link['href'])
#                     if urlparse(full_link).netloc == urlparse(base_url).netloc:
#                         junk_words = ['replytocom', '.jpg', '.png', '.pdf', '/tag/', '/category/', '/author/']
#                         if not any(word in full_link for word in junk_words) and full_link not in visited:
#                             to_visit.append(full_link)
            
#             time.sleep(0.5)
#         except Exception as e:
#             print(f"❌ Error: {current_url}: {e}")

#     print(f"🏁 Scraper Finished. Total {scraped_count} pages checked.")
#     return any_file_updated # Batayega ke DB update karni hai ya nahi

# if __name__ == "__main__":
#     updated = scrape_zt_hosting()
#     if updated:
#         print("🔄 Changes detected! Triggering Ingest...")
#         # Yahan ingest.py ko call karne ka code ayega
#     else:
#         print("😴 No changes on website. DB is already up to date.")


# Aapka scraper.py code kaafi mature hai, lekin automation ko full-fill karne ke liye humein ismein ingest.py ko trigger karne ka logic aur file paths ko thora robust banana hoga.

# Niche diya gaya updated code automatically ingest.py ko tabhi run karega jab koi real change detect hoga.


import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse
import time
import hashlib
import subprocess # Naya: ingest.py ko run karne ke liye

def get_content_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def scrape_zt_hosting():
    base_url = "https://zthosting.com/"
    visited = set()
    to_visit = [base_url]
    MAX_PAGES = 100
    scraped_count = 0
    any_file_updated = False 

    # Path ko dynamic banaya taake GitHub Actions aur local dono par chale
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # data_folder = os.path.join(current_dir, '..', 'data', 'scraped_pages')

    data_folder = os.path.join(current_dir, '..', 'data')
    
    if not os.path.exists(data_folder): 
        os.makedirs(data_folder)

    print(f"🚀 Daily Sync Scraper started...")

    while to_visit and scraped_count < MAX_PAGES:
        current_url = to_visit.pop(0)
        if current_url in visited or "#" in current_url: continue
            
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(current_url, headers=headers, timeout=10)
            visited.add(current_url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                path = urlparse(current_url).path.strip('/')
                file_name = f"{path if path else 'zt_home_page'}.txt".replace('/', '_')
                file_path = os.path.join(data_folder, file_name)
                
                content = soup.find('main') or soup.find('article') or soup.body
                if content:
                    text_data = content.get_text(separator='\n', strip=True)
                    new_hash = get_content_hash(text_data)
                    
                    should_write = True
                    if os.path.exists(file_path):
                        with open(file_path, "r", encoding="utf-8") as f:
                            old_content = f.read()
                            if new_hash in old_content: 
                                should_write = False

                    if should_write:
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(f"Source: {current_url}\nHash: {new_hash}\n" + "="*30 + "\n" + text_data)
                        any_file_updated = True
                        print(f"✨ Updated: {file_name}")
                    
                    scraped_count += 1

                for link in soup.find_all('a', href=True):
                    full_link = urljoin(base_url, link['href'])
                    if urlparse(full_link).netloc == urlparse(base_url).netloc:
                        junk_words = ['replytocom', '.jpg', '.png', '.pdf', '/tag/', '/category/', '/author/']
                        if not any(word in full_link for word in junk_words) and full_link not in visited:
                            to_visit.append(full_link)
            
            time.sleep(0.5)
        except Exception as e:
            print(f"❌ Error: {current_url}: {e}")

    print(f"🏁 Scraper Finished. Total {scraped_count} pages checked.")
    return any_file_updated

if __name__ == "__main__":
    updated = scrape_zt_hosting()
    
    if updated:
        print("🔄 Changes detected! Triggering Ingest...")
        # ingest.py ka sahi path check karein (agar wo scraper folder se bahar hai)
        ingest_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'ingest.py')
        
        # Ingest trigger logic
        try:
            subprocess.run(["python", ingest_path], check=True)
            print("✅ Ingest completed successfully.")
        except Exception as e:
            print(f"⚠️ Ingest failed: {e}")
    else:
        print("😴 No changes on website. DB is already up to date.")