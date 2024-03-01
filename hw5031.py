import timeit
from collections import Counter
import requests

def brute_force_search(text, pattern):
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            occurrences.append(i)
    return occurrences

def kmp_search(text, pattern):
    occurrences = []
    n, m = len(text), len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            occurrences.append(i - m + 1)
            q = pi[q - 1]
    return occurrences

def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k
    return pi

def rabin_karp_search(text, pattern):
    occurrences = []
    n, m = len(text), len(pattern)
    pattern_hash = hash(pattern)
    for i in range(n - m + 1):
        if hash(text[i:i+m]) == pattern_hash and text[i:i+m] == pattern:
            occurrences.append(i)
    return occurrences

# Load text from URLs
url_article1 = "https://drive.google.com/uc?export=download&id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"
url_article2 = "https://drive.google.com/uc?export=download&id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ"

def get_text_from_url(url):
    response = requests.get(url)
    return response.text if response.status_code == 200 else ""

article1 = get_text_from_url(url_article1)
article2 = get_text_from_url(url_article2)

# Define patterns
pattern1 = "search"
pattern2 = "algorithm"

# Measure execution time
search_algorithms = {
    "Brute Force": brute_force_search,
    "KMP": kmp_search,
    "Rabin-Karp": rabin_karp_search
}

results = {}
for algorithm, search_func in search_algorithms.items():
    results[algorithm] = {}
    for text_name, text in [("Article 1", article1), ("Article 2", article2)]:
        time_taken = timeit.timeit(lambda: search_func(text, pattern1), number=10)
        results[algorithm][text_name] = time_taken

# Find the fastest algorithm for each text
fastest_algorithms = {text_name: min(results.keys(), key=lambda x: results[x][text_name]) for text_name in ["Article 1", "Article 2"]}

# Generate markdown report
report = f"# Search Algorithms Performance Report\n\n"
report += "## Fastest Algorithms:\n"
for text_name, fastest_algorithm in fastest_algorithms.items():
    report += f"- {text_name}: {fastest_algorithm}\n"
report += "\n## Detailed Results:\n"
for algorithm, timings in results.items():
    report += f"### {algorithm}:\n"
    for text_name, time_taken in timings.items():
        report += f"- {text_name}: {time_taken:.6f} seconds\n"

# Save report to a markdown file
with open("search_algorithms_report.md", "w", encoding="utf-8") as file:
    file.write(report)

# Print report as a docstring
print(f"'''\n{report}\n'''")

