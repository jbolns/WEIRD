(BTW. This page comes from a .md document)
## HOW TO > *Prerequisites*
**1 [Python](https://www.python.org/downloads/),** including:

* [Beautiful soup](https://pypi.org/project/beautifulsoup4/) - *pip install beautifulsoup4*
* [Docx2Python](https://pypi.org/project/docx2python/) - *pip install docx2python*
* [Markdown](https://pypi.org/project/Markdown/) - *pip install Markdown*
* [Pywin32](https://pypi.org/project/pywin32/) - *pip install pywin32.*

**2 [WEIRD](https://github.com/jbolns/weird).**

* Fork/download/save WEIRD anywhere on your computer.
  
**3** At least one **content document for the home page.**

* It is possible to upload more documents/pages, but you need at least one document for the home page. 
* Do NOT use the word *"blog"* in document names.
* Supported formats: .html, .md, .docx, .docm.

**4 Logo** (300x300px), **emoticon** (75x75px), and **social media preview** (circa 1200x630px) images.

---

## HOW TO > *Set up a new WEIRD website (low-code)*
Open WEIRD's folder and launch a terminal. Then...

### Configuration
Run the configuration assistant: **python config.py**. 

Answer questions. Follow instructions. It's a surprisingly painless process. Probably easier to understand than this guide. 

That said, if you absolutely need a preview, it goes like this.

**Required steps.**

*	***System info.*** The assistant will ask about the name, author, type, and keywords for the websites, as well as the title and introduction for the header.
*	***Blog settings.*** The assistant will then ask if the website needs a blog.
*	***Images.*** Finally, the assistant will ask for the three images noted above as requirements.

**Optional steps.**

* ***Social media.*** The assistant will ask for the links for desired social media channels.
* ***Pages.*** The assistant will ask for documents to set up as pages. It will also ask if images were referenced in HTML or Markdown documents (relative path: ../images/pages/filename), in which case it will open a file explorer to upload the images.
* ***Blog entries.*** The assistant will ask for documents to set up as blog entries. It will also ask if images were referenced in HTML or Markdown documents (relative path: ../images/blog/filename), in which case it will open a file explorer to upload the images.

### Build
Run the build assistant and follow any instructions: **python build.py**.

The only thing the build assistant will ask is for the author, date, and categories of any blog entries NOT in Markdown (for Markdown documents, use Markdown's author, date, and categories meta-information syntax). 

If there are no such documents, the assistant will not ask anything.

### Serve
Weird comes with a local server. To run: **python -m http.server**.

Unfortunately, we haven't yet configured an assistant to facilitate hosting. You're going to have to figure this out by yourself. WEIRD produces static websites, though. Should be straightforward.

---

## HOW TO > *Update an existing WEIRD website (low-code)*
The assistants in the previous sections re-write the settings and re-create the entire build. This is inconvenient if all you want is to update or add to the websites.

### Incremental updates
To update or add pages or blogs without re-writing the entire build, run: **python add.py**.

It's a surprisingly painless process. 

To add a page or a blog add a new document with a different filename than existing ones. To update an existing page or blog entry, simply use the filename of an existing page/blog.

The flow of actions is pretty much the same as described in earlier sections

* **Type.** Assistant asks if you are creating/updating a page or a blog entry
* **Document.** The assistant initiates a file explorer for you to upload the document
* **Images.** The assistant asks for any images referenced in HTML or Markdown code (relative path: ‘../images/pages/filename’ or ‘../images/blog/filename’, as appropriate)
* **Meta-information.** When uploading a blog entry NOT written in Markdown, the assistant asks for author, date, and categories for it.

---

## HOW TO > *Reset an existing WEIRD website (low-code)*

To clear a biuld or the entire configuration for a WEIRD website, run: **python reset.py**.

This will clear any pre-existing build regardless. It will also ask you if you want to delete non-core files. If you answer 'yes', the WEIRD folder will be reset entirely.

---

## HOW TO > *Use WEIRD solely as a web framework (coding required)*

If you know Python, HTML, CSS, and JS, you can skip all the assistants and use WEIRD only as a web framework.

Pending.

.

.