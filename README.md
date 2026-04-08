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