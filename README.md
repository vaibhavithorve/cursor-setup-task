# cursor-setup-task
## Tools Installed
- **Cursor IDE** — AI-powered code editor
- **Git** — version control system required to clone GitHub repositories into Cursor
- **GitHub** — cloud platform to host the repository
- **VS Code** — installed as the default editor for Git
- **Claude** — already had this installed prior to the task
- **Claude Code extension** (by Anthropic) — installed via Cursor's Extensions panel
- **Codex extension** (by OpenAI) — installed via Cursor's Extensions panel

## Steps Completed
1. Downloaded and installed Cursor IDE, completing the setup prompts during installation
2. Created a GitHub account and set up a new **public** repository with the README.md option enabled
3. Installed the **Claude Code** extension (by Anthropic) from Cursor's Extensions panel
4. Installed the **Codex** extension (by OpenAI) from Cursor's Extensions panel
5. Cloned the GitHub repository into a local folder and opened it in Cursor
6. Edited this README.md file to document the full setup process and committed + pushed to GitHub

## Issues Encountered & How I Solved Them

**1. Which Claude Code extension to install**
Searching "Claude Code" in Cursor's Extensions panel returned multiple results from different
publishers, making it unclear which one to choose. I did several Google searches and couldn't
find a definitive answer. I then brought the problem to Claude (Cowork), explained the exact
options I was seeing, and specifically mentioned who made each extension. Claude advised me to
go with the official **Claude Code by Anthropic** and avoid third-party versions. Applied the
same logic for Codex — went with the one by **OpenAI**.

**2. Git was required to clone a GitHub repository into Cursor**
After creating my GitHub repository and logging in, I couldn't figure out how to clone it into
Cursor. I went through several YouTube videos and Google searches. Eventually I came across an
option inside Cursor that prompted me to download Git. I looked into whether Git was actually
necessary — it is. Downloading and installing Git resolved the issue and allowed me to proceed
with cloning.

**3. Cloning the repository into Cursor**
The most commonly suggested method online was to press `Ctrl + Shift + P` to open the Command
Palette in Cursor, type `Git: Clone`, and paste the HTTPS link from GitHub. I tried this but
the repository was not cloning successfully. After more research, I found a method that worked:
cloning the repository into a local folder first, and then opening that folder in Cursor. This
approach worked correctly.

**4. Committing and pushing changes**
When I was ready to commit, Cursor initially did not load the changes in the Source Control
panel. I started looking into manual ways to commit via the terminal, but by the time I
returned from researching, the README.md file had appeared under Changes on its own. I clicked
the **+** button to stage it and typed a commit message — but hit another issue: Git did not
have my username and email configured, which is required before making a commit.

I watched a YouTube video that showed the fix — running these two commands in the terminal:
git config --global user.name "your username"
git config --global user.email "your email"

However, when I ran them, I got an error saying Git was not recognized as a cmdlet, function,
script file, or operable program. This meant the terminal wasn't picking up Git even though it
was installed.

I found a blog post that explained the fix: the environment variables (which tell the terminal
where Git is installed) had not been loaded yet. The solution was to:
1. Restart Cursor to refresh the environment variables
2. Go into Cursor's settings and enable the **legacy terminal** option

After doing both of these, the terminal recognized Git, the config commands ran successfully,
and I was able to stage, commit, and push the changes to GitHub without any further issues.

## Research Project: AI-Powered SEO Content Production

### Topic
AI-Powered SEO Content Production — how practitioners use AI tools, workflows,
and systems to research, write, optimize, and scale content that ranks on
Google and gets cited by LLMs like ChatGPT and Perplexity.

---

### Why I Chose This Topic

AI-powered SEO content production is where search is heading. Traditional SEO
is no longer just about keywords and backlinks — it now involves understanding
how LLMs evaluate and cite content, how to build topical authority at scale
using AI tools, and how to create content workflows that produce quality output
efficiently. This is the most practical, future-facing angle I could research
given where Google and AI search are moving together.

---

### How I Collected the Content

**YouTube Transcripts — Python Script via API**

I used the `youtube-transcript-api` Python library to collect transcripts
programmatically. I wrote a custom Python script (`scripts/fetch_transcripts.py`)
that fetched transcripts for 28 videos across 8 YouTube creators and
automatically saved them into organized subfolders by creator name inside
`research/youtube-transcripts/`.

Problems I ran into and how I solved them:

- **Python not installed** — pip and python commands were not recognized in the
  terminal. I downloaded and installed Python from python.org, making sure to
  tick "Add Python to PATH" during installation, and also allowed long path
  support when prompted by Windows.

- **youtube-transcript-api method changed** — after installing the library and
  running the script, all 28 transcripts failed with the error: "type object
  YouTubeTranscriptApi has no attribute get_transcript". This was because the
  library had been recently updated and the API changed. The old method
  `YouTubeTranscriptApi.get_transcript(video_id)` was replaced with a new
  approach requiring the class to be instantiated first:
  `ytt_api = YouTubeTranscriptApi()` followed by `ytt_api.fetch(video_id)`.
  I updated the script accordingly and all transcripts ran successfully.

- **Supadata MCP setup issues** — I also set up Supadata as an MCP tool inside
  Cursor IDE as a backup transcript method. This required installing Node.js
  first (which was not installed), then fixing a config error where the
  environment variable was named `X_API_KEY` instead of the required
  `SUPADATA_API_KEY`. After both fixes, Supadata connected successfully.
  However I ultimately used the Python script for all transcript collection
  to avoid consuming Cursor's free plan agent credits.

**LinkedIn Posts — Manual Collection**

LinkedIn blocks automated scraping, so I manually collected posts from the
three LinkedIn-active creators in my list. I also saved two PDF carousel posts
directly from LinkedIn — one from Scalerrs on how to write LLM-cited content,
and one from Madhurima Halder (Authority Juice) documenting a real client case
study showing how a SaaS brand went from 22 organic clicks/month to 10.6K+
clicks and AI citation alongside Buffer and Hootsuite in under 12 months.

**Git and Repository Setup Issues**

During repo setup I also encountered and resolved:

- An accidentally created "Untitled" file from clicking in Cursor's UI — removed
  with `git rm Untitled`
- The `sources.md` file being committed while still empty — caught by checking
  GitHub directly, then added the content and recommitted
- Learning that GitHub does not display empty folders — only files appear, so
  the folder structure only became visible once transcript files were added

---

### The 10 Experts I Chose and Why

These are not experts I found through a Google search. These are creators and
practitioners I have personally followed, subscribed to, and learned from over
time. Every practical SEO and content skill I have — keyword research, content
structuring, ranking strategy, AI content workflows — traces back to people on
this list. I can vouch for their content because I have applied it and seen it
work.

---

**1. Collin SEO (Alex Collins Alonso)**
YouTube: https://www.youtube.com/@COLLINSEO

The creator I credit most for teaching me how content actually ranks. He takes
a psychological and analytical approach to SEO and only shares strategies he
has personally tested with clients. His free worksheets and tutorials on keyword
research, semantic positioning, content clustering, and outline creation gave me
my foundational understanding of SEO content. His video on using ChatGPT to
create Google-friendly SEO pages was one of the first pieces of content that
showed me how to use AI properly for content production. Small subscriber count
but the knowledge is vast, tried, tested, and genuinely works — I have applied
it myself.

Assigned workflow phase: Keyword Research + AI Content Production

---

**2. Matt Diamante**
YouTube: https://www.youtube.com/@heymattdiamante

I purchased his course and applied his methods directly on a real brand I was
working with. His core argument is that ranking is more achievable than most
people make it seem, and he backs this with specific quick-fix techniques. His
advice on using Reddit as part of an SEO and content strategy produced a
measurable increase in traffic for a brand I managed — which gave me direct
evidence that his approach is grounded in practice, not theory.

Assigned workflow phase: Content Optimization + Quick Ranking Fixes

---

**3. Vasco's SEO Tips**
YouTube: https://www.youtube.com/@VascoSEOtips

Vasco shares what worked in his own SEO practice and shows exactly how he did
it — no padding, no theory. I have learned many of my core content strategies
from his videos. Most relevant for this research: he has recently been producing
a large amount of content specifically about using AI and Claude for SEO content
production, making his recent videos directly applicable to the topic.

Assigned workflow phase: AI Content Production Workflows (Claude + AI tools)

---

**4. Elena Dyulgerova + Scalerrs Agency**
LinkedIn: https://www.linkedin.com/in/elena-dyulgerova
LinkedIn: https://www.linkedin.com/company/scalerrs-agency

Elena leads SEO and AEO at Scalerrs, an agency built on the belief that search
has fundamentally changed and strategy must evolve with it — focusing on Reddit
SEO, Answer Engine Optimization, and AI-integrated content. Scalerrs is the
LinkedIn content I engage with most consistently and the primary reason I open
LinkedIn. Their posts are entirely case-driven — real client problems, real
strategies, real results. They share failures alongside wins and publish brand
breakdowns openly, which trained me to think analytically about SEO problems.

Assigned workflow phase: Modern Search Strategy (AEO, Reddit, AI Overviews)

---

**5. Exposure Ninja**
YouTube: https://www.youtube.com/@ExposureNinja

A full-service search marketing agency with real clients and real results.
Their YouTube channel covers the complete SEO spectrum — from keyword research
to AI overview optimization to blog content — all backed by agency experience.
I learned from their detailed, process-driven content that shows actual workflows
rather than just concepts.

Assigned workflow phase: Agency SEO Production + AI Overview Strategy

---

**6. Create and Grow**
YouTube: https://www.youtube.com/@createandgrowshow

A podcast channel that brings in real practitioners — people actively working
with brands on SEO, content, and organic growth — for unscripted, unedited
conversations about their actual strategies. The raw format means guests speak
openly about what worked and why in a way polished tutorials rarely allow. I
only collected episodes specifically focused on SEO content strategy, AI content
production, and backlink approaches.

Assigned workflow phase: Broader Strategic Perspectives (practitioner interviews)

---

**7. Nathan Gotch**
YouTube: https://www.youtube.com/@nathangotch

One of the most recognized names in SEO education and for good reason — his
content is detailed, accurate, and consistently grounded in tactics he has used
himself through his agency Gotch SEO. His tutorials cover the full SEO spectrum
without bloat. Well known across the SEO community and consistently cited as a
trusted reference.

Assigned workflow phase: Content Strategy + SERP Analysis

---

**8. Madhurima Halder (Authority Juice)**
LinkedIn: https://www.linkedin.com/in/madhurima-halder/

Founder of Authority Juice, helping B2B startups grow organic presence without
paid ads. Her LinkedIn content is built entirely around real client strategies —
what she tried, how it worked, and why. She is the second creator I follow most
consistently on LinkedIn after Elena. Her content pushes me to think differently
rather than just confirming what I already know. I saved a full case study she
posted documenting how a SaaS client (Distribution.ai) went from 22 organic
clicks/month and near-zero AI visibility to 10.6K+ clicks/month and being cited
by Google AI Overviews alongside Buffer and Hootsuite — all in under 12 months.

Assigned workflow phase: B2B Content Authority + Real Client Case Studies

---

**9. TM Blast (Greg Kristan)**
YouTube: https://www.youtube.com/@tmblast

Greg has run TM Blast since 2017, working with local, B2B, and B2C SEO clients.
He shares knowledge freely and in depth without holding back specifics the way
many agency owners do. His content on local SEO gave me a strong foundation for
understanding how search intent and geographic context affect content strategy —
knowledge that directly informs how AI-powered content should be adapted for
different client types.

Assigned workflow phase: Systematic SEO Production + Local SEO

---

**10. Aleyda Solis**
YouTube: https://www.youtube.com/@aleydasolis
LinkedIn: https://www.linkedin.com/in/aleydasolis/

International SEO consultant and founder of Orainti. One of the few
practitioners who publicly documents the exact AI workflows she uses with
clients — including actual prompts, processes, and results. Her content on
using AI for content briefs, content production, and technical audits is
directly applicable to this research and represents the highest level of
AI-SEO integration available in public practitioner content.

Assigned workflow phase: AI Prompting Workflows + Professional Benchmark

---

### What Was Collected

| Creator | Platform | Files Collected |
|---|---|---|
| Collin SEO | YouTube | 5 transcripts |
| Matt Diamante | YouTube | 3 transcripts |
| Vasco's SEO Tips | YouTube | 4 transcripts |
| Elena / Scalerrs | LinkedIn | Posts + PDF carousel |
| Exposure Ninja | YouTube | 4 transcripts |
| Create and Grow | YouTube | 3 transcripts |
| Nathan Gotch | YouTube | 5 transcripts |
| Madhurima Halder | LinkedIn | Posts + client case study PDF |
| TM Blast | YouTube | 2 transcripts |
| Aleyda Solis | YouTube + LinkedIn | 2 transcripts + posts |

**Total: 28 YouTube transcripts + LinkedIn posts + 2 PDF case studies**

---

### Why This Library is Strong Enough for a Playbook

Each creator was assigned a specific phase of the AI-powered SEO content
production workflow — keyword research, SERP analysis, content brief creation,
AI production, optimization, distribution, and measurement. The library covers
the full workflow from different angles: solo educators, agency owners, B2B
consultants, and podcast practitioners. The LinkedIn case studies add real
before/after data from actual clients. Together this is not a random collection
of SEO content — it is a mapped, phase-by-phase research base that can directly
support building an AI-powered SEO content production playbook.