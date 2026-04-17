from youtube_transcript_api import YouTubeTranscriptApi
import os

# Create subfolders for each creator
creators = [
    "collin-seo",
    "matt-diamante",
    "vasco-seo-tips",
    "exposure-ninja",
    "create-and-grow",
    "nathan-gotch",
    "tm-blast",
    "aleyda-solis"
]

for creator in creators:
    os.makedirs(f"research/youtube-transcripts/{creator}", exist_ok=True)

# All videos organized by creator
videos = {

    # COLLIN SEO - Keyword Research + AI Content Production
    "collin-seo/collin-video-1": "SK6hJeQW_bY",
    "collin-seo/collin-video-2": "fx1vn8oWXTA",
    "collin-seo/collin-video-3": "0oAFj97Hurk",
    "collin-seo/collin-video-4": "sBTAwCjwg_c",
    "collin-seo/collin-video-5": "4do6998ldZ0",

    # MATT DIAMANTE - Content Optimization + Quick Ranking Fixes
    "matt-diamante/matt-video-1": "RlWDeKwyBh0",
    "matt-diamante/matt-video-2": "IjTaTDpRrME",
    "matt-diamante/matt-video-3": "vr_LgnOq4tw",

    # VASCO SEO TIPS - AI Content Production Workflows
    "vasco-seo-tips/vasco-video-1": "JLBp3tB2P1E",
    "vasco-seo-tips/vasco-video-2": "vpV_W23hGGE",
    "vasco-seo-tips/vasco-video-3": "dXhUg9Eu0xM",
    "vasco-seo-tips/vasco-video-4": "woJaCDgrgPU",

    # EXPOSURE NINJA - Modern Search Strategy + AI Overviews
    "exposure-ninja/exposure-ninja-video-1": "eJGRFlmtOd4",
    "exposure-ninja/exposure-ninja-video-2": "8VMSyHS5RhM",
    "exposure-ninja/exposure-ninja-video-3": "SIsr8c6WLC4",
    "exposure-ninja/exposure-ninja-video-4": "uuChqdkg5gU",

    # CREATE AND GROW - Broader Strategy Perspectives
    "create-and-grow/create-and-grow-video-1": "pXXBj6W87FE",
    "create-and-grow/create-and-grow-video-2": "0PlXvzi7T9Q",
    "create-and-grow/create-and-grow-video-3": "1PfHkYq3vSc",

    # NATHAN GOTCH - Content Strategy + SERP Analysis
    "nathan-gotch/nathan-video-1": "Fh_54G6p_cs",
    "nathan-gotch/nathan-video-2": "4tqCKkGilXI",
    "nathan-gotch/nathan-video-3": "JHBZfT9--ZE",
    "nathan-gotch/nathan-video-4": "77xJdk7DTUc",
    "nathan-gotch/nathan-video-5": "NX3fKffuHwg",

    # TM BLAST - Systematic SEO Production
    "tm-blast/tm-blast-video-1": "BxVfGc7Uq3w",
    "tm-blast/tm-blast-video-2": "QUptEAtrwD8",

    # ALEYDA SOLIS - AI SEO Workflows + Prompting
    "aleyda-solis/aleyda-video-1": "lEtXlk0XTsI",
    "aleyda-solis/aleyda-video-2": "3xa199rr3zo",
}

# Fetch and save all transcripts
success = 0
failed = 0

print(f"\nFetching {len(videos)} transcripts...\n")

# New API usage - instantiate the class first
ytt_api = YouTubeTranscriptApi()

for filename, video_id in videos.items():
    try:
        transcript = ytt_api.fetch(video_id)
        full_text = " ".join([snippet.text for snippet in transcript])

        output_path = f"research/youtube-transcripts/{filename}.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"Source: https://www.youtube.com/watch?v={video_id}\n")
            f.write(f"File: {filename}\n")
            f.write("-" * 50 + "\n\n")
            f.write(full_text)

        print(f"✓ {filename}")
        success += 1

    except Exception as e:
        print(f"✗ {filename} — {e}")
        failed += 1

print(f"\n--- Done ---")
print(f"✓ Success: {success}")
print(f"✗ Failed: {failed}")