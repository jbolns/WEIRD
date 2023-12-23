# WEIRD
A Python-meets-Javascript **multi-modal web framework**.

WEIRD is coded in layers, very onion-like. You can use it as a low-code tool to make websites easily from a variety of documents *or* skip the assistants altogether to use purely as a web framework.

Yeah, we get it. WEIRD is weird.

But it can produce surprisingly good and fairly sustainable websites from little more than just a few documents (even Word documents!).

>*Ps1. Current version: Beta -7.*

>*Ps2. A more detailed explanation of WEIRD is available after the HOW TO section below.*

---
---

## HOW TO > Prerequisites
* [Python](https://www.python.org/downloads/), including:
  * [Beautiful soup](https://pypi.org/project/beautifulsoup4/) - *pip install beautifulsoup4*
  * [Docx2Python](https://pypi.org/project/docx2python/) - *pip install docx2python*
  * [Markdown](https://pypi.org/project/Markdown/) - *pip install Markdown*
  * [Pywin32](https://pypi.org/project/pywin32/) - *pip install pywin32.*
* [WEIRD](https://github.com/jbolns/weird). 
  * Fork/download/save WEIRD anywhere on your computer.
* At least **one document** with content for the **home page**.
  * It is possible to upload more documents/pages, but you need at least a *home* page. 
  * Do NOT use the word *"blog"* in document names.
  * Currently supported formats: .html, .md, .docx, .docm.
* Images for the **logo** (300x300px), **emoticon** (75x75px), and **social media** (1200x630px).

## HOW TO > Set up a new WEIRD website (low-code)
Open WEIRD's folder and launch a terminal. Then...

### Configuration
Run the configuration assistant. Answer questions. Follow instructions. It's a surprisingly painless process. Probably easier to understand than this guide.
```
python config.py
```

If you absolutely need a preview, it goes like this.

* Required steps.
  *	The assistant will ask about the name, author, type, and keywords for the websites, as well as the title and introduction for the header.
  *	The assistant will then ask if the website needs a blog.
  *	Finally, the assistant will ask for the three images noted above as requirements.
* Optional steps.
  *	*Social media.* The assistant will ask for the links for desired social media channels.
  * *Pages.* The assistant will ask for documents to set up as pages. It will also ask if images were referenced in HTML or Markdown documents (relative path: ../images/pages/filename), in which case it will open a file explorer to upload the images.
  * *Blog.* The assistant will ask for documents to set up as blog entries. It will also ask if images were referenced in HTML or Markdown documents (relative path: ../images/blog/filename), in which case it will open a file explorer to upload the images.
  
### Build
Run the build assistant and follow any instructions.
```
python build.py
```
If you absolutely need a preview, it goes like this.

*	**Blog meta-information.** The assistant will ask for the author, date, and categories of any blog entries NOT in Markdown (for Markdown documents, just use the standard author, date, and categories meta-information syntax).
* If there are no such documents, the assistant will not ask for anything.

### Serve
Weird comes with a local server. To run: 
```
python -m http.server
```
Unfortunately, we haven't yet configured an assistant to facilitate hosting. You're going to have to figure this out by yourself. 

WEIRD produces static websites, though. Should be straightforward: save files to bucket or hosting service, done. 

That said, please note WEIRD is configured to work at the root of a domain/localhost (e.g. example.com). Subdomains (e.g. weird.example.com) work, or at least we think they do (we use a subdomain to host WEIRD's public website). However, to upload a WEIRD website to a folder of a domain (e.g. example.com/weirdsite) you would need to re-write the main.js file to account for path differences. We tried. It wasn't worth it.

## HOW TO > Update an existing WEIRD website (low-code)
The assistants in the previous sections re-write the settings and re-create the entire build. This is inconvenient if all you want is to update or add to the websites.

### Incremental updates
To update or add pages or blogs without re-writing the entire build, run: 
```
python add.py.
```
Again, the assistant is fairly easy to follow. As long as you have a document to upload and any associated images, you probably will be fine. 

But if you absolutely need a preview, it goes like this.
* **Type.** The assistant will ask whether you want to upload a new page or a new blog (to update an existing page/blog, use the filename of the existing page/blog)
* **Document.** The assistant will ask you to upload the document
* **Images.** The assistant will ask you to upload any images referenced in HTML or Markdown code (relative path: ‘../images/pages/filename’ or ‘../images/blog/filename’, as appropriate)
* **Meta-information.** If you are uploading a blog not written in Markdown, the assistant will ask for author, date, and categories for it.


## HOW TO > *Reset an existing WEIRD website (low-code)*

To clear a build or the entire configuration for a WEIRD website, run: **python reset.py**.

This will clear any pre-existing build regardless. It will also ask you if you want to delete non-core files. If you answer 'yes', the WEIRD folder will be reset to factory settings.

## HOW TO > Use WEIRD as a web framework (coding required)
If you know Python, HTML, CSS, and JS, you can skip all the assistants and use WEIRD only as a web framework.

Pending.

.

.

---
---

## But seriously, what is WEIRD?
WEIRD is both a no-code/low-code tool to make websites easily from a variety of documents *and* a web framework developers can use to code websites.

It depends on how you use it.

* **No-code/low-code tool:** WEIRD comes with chat-based assistants anyone can use to easily build websites by answering questions and uploading documents/images. You could, in theory, build a website from Word documents alone. The formatting in Word (.docm) documents tends to come through. Given some trial and error, thus, Word could become your new 'WYSIWYG' editor.

* **Web-framework:** WEIRD's weird because it combines programming languages not often combined: Python, HTML/CSS/JS, and VBA. That said, WEIRD is coded in an onion-like manner that makes it possible for developers to customise WEIRD layer by layer. Web developers can personalise WEIRD websites using HTML, CSS, JS, and libraries such as jQuery and Bootstrap. Python developers can tinker with the build process. VBA developers can play around with how WEIRD and Office communicate, paving the way for personalised interactions between their websites and Office documents.

* **Something in between:** Since document types can be combined, WEIRD is a way for coders (especially those with little time availability) to focus coding on key website sections while reducing the time needed to manage other sections. Alternatively, WEIRD might also be helpful in facilitating collaboration by teams from diverse technical backgrounds: some can upload code, others, documents.

Something else that is noteworthy is that WEIRD can produce websites that are more sustainable than the average, as measured by appropriate third-party tools. WEIRD's maker J wanted a website that was far more sustainable than the average, but he also wanted to avoid hard-coding things (it gets very repetitive). WEIRD is the result of trying to find automated ways to code a highly sustainable website.

Not to say that all WEIRD websites will be sustainable. Usage matters. However, used well, WEIRD can produce fairly sustainable websites.

## Examples

**[WEIRD](https://weird.polyzentrik.com)**
* WEIRD's public website was produced with WEIRD, of course.
* It is an example of the foundational type of website WEIRD produces without customisation.  

**[Dr J](https://www.josebolanos.xyz/)**
* WEIRD's maker's website was made with a modified WEIRD that renders app-like websites (only content refreshes when clicking links). It also is one of the most sustainable websites in the planet.
* It is an example of a website using WEIRD as a web framework with significant room for customisation.

.

Submissions welcome. Get in touch somehow. 

## BUT keep in mind, WEIRD is not REACT
WEIRD produces static websites and is best-suited for small-to-medium websites. The kind of websites that come to mind when thinking, for example, about portfolios, project and landing pages, documentation, personal blogs, and some SME websites. For larger websites and/or websites requiring dynamic interactions between front and back end, you need something different.

Furthermore, WEIRD's current version is Beta -7. We believe WEIRD can already be useful in many circumstances, but we also advice treating it as the experimental product that it is.

## License
WEIRD is a product by [polyzentrik.com](https://www.polyzentrik.com/), released under an Apache 2.0 open source license.

We kindly ask you to leave the branding in the footer intact or [make a small voluntary payment via our main website](https://www.polyzentrik.com/help-us-help/) if you wish to remove it. This is not a legal obligation, but it would be quite nice.
