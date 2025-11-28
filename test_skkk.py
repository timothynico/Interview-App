from scrap_website import scrape_skkk_data
import json

# Test scraping dengan NRP
test_nrp = "C14220062"

print(f"Testing SKKK scraping untuk NRP: {test_nrp}\n")
result = scrape_skkk_data(test_nrp)

print("=== Result ===")
print(f"Success: {result['success']}")
print(f"Total Activities: {result['total_activities']}")

if result['success']:
    print("\n=== SKKK Data ===")
    for i, activity in enumerate(result['data'][:5], 1):  # Show first 5 activities
        print(f"\n{i}. {json.dumps(activity, indent=2, ensure_ascii=False)}")

    if result['total_activities'] > 5:
        print(f"\n... dan {result['total_activities'] - 5} kegiatan lainnya")
else:
    print(f"Error: {result.get('error', 'Unknown error')}")
