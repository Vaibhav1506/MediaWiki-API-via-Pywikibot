import pywikibot
import stats

def return_num(text, idx):
    num = ''
    while idx < len(text) and text[idx] != '"':
        num += text[idx]
        idx += 1
    return num

def main():
    # Connect to the site using the user-config.py settings
    site = pywikibot.Site()
    site.login()

    # Target page title
    page_title = "Template:WikiStatistics"

    # Load the page
    page = pywikibot.Page(site, page_title)
    stats_list = stats.get_data()
    original_text = page.text  # Save original for comparison
    text = original_text

    # Find index positions
    rc_idx = text.find("Number of Ratings") + 109
    upv_idx = text.find("Number of Upvotes") + 109
    downv_idx = text.find("Number of Downvotes") + 111

    # Extract old values
    prev_rc = return_num(text, rc_idx)
    prev_upv = return_num(text, upv_idx)
    prev_downv = return_num(text, downv_idx)

    print(f"Previous: Ratings={prev_rc}, Upvotes={prev_upv}, Downvotes={prev_downv}")
    print(f"New: Ratings={stats_list[0]}, Upvotes={stats_list[1]}, Downvotes={stats_list[2]}")

    # Replace with new values
    text = text.replace(prev_rc, stats_list[0])
    text = text.replace(prev_upv, stats_list[1])
    text = text.replace(prev_downv, stats_list[2])

    # Only save if changes were actually made
    if text != original_text:
        page.text = text
        page.save(summary="Updated Wiki Statistics")
        print("Page updated.")
    else:
        print("No changes detected. Page not saved.")

if __name__ == '__main__':
    main()
