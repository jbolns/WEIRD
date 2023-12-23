// MAIN JS FILE
// .................
// .................



// .................
// LOAD & RELOAD   :
// .................
// .................
// To avoid repainting everything every time a user clicks a link, this website does not have standard links
// Instead, links call a function that loads/reloads the main section only
// .......................................................................


// FUNCTION TO HANDLE THE BASIC LOADING OF PAGES
async function load() {
  // Get relative path
  const pre = location.pathname === '/' ? '.' : '..'

  // Get/write body elements: <header>, <main>, <footer>
  const header = await $.get(`${pre}/components/header.html`, function (data) {
    return data
  })

  const main = await $.get(`${pre}/components/main.html`, function (data) {
    return data
  })

  const footer = await $.get(`${pre}/components/footer.html`, function (data) {
    return data
  })

  await $('body').prepend(header + main + footer)

  // Get/write main navigation links
  const page = location.pathname.slice(location.pathname.lastIndexOf('/') + 1)
  toplinks('nav1.json', '.toplinks', pre)
  toplinks('socials.json', '.socials', pre)

  // Get/write content of main section
  if (location.pathname === '/') {
    $('#wrapper').load('./components/home.html')
  } else {
    console.log('pathname is... ', location.pathname)
    $('#wrapper').load(`${pre}/components/${page}`)
  }

}

// FUNCTION TO LOAD HEADER AND FOOTER NAV & SOCIAL LINKS
async function toplinks(path, selector, pre) {
  // Call function to get links and link names
  const entries = await $.ajax(pre + '/json/' + path)
    .done(function (response) {
      console.log('Call to links JSON successfull, response:', response)
    })
    .fail(function () { console.log('error with ajax call') })

  // Load and write links
  if (selector === '.toplinks') {
    let write = `<li class='open' onclick='openMenu()'>
          <img src='${pre}/images/list.webp' alt='Open' width='50' height='50'>
        </li>
        <li class='close' onclick='closeMenu()'>
          <img src='${pre}/images/x-square-fill.webp' alt='Close' width='50' height='50'>
        </li>`
    $('header > nav >' + selector).append(write)
  }

  if (selector === '.toplinks') {
    let write = `<li class='wide'><a href='/'>home</a></li>`
    $(selector).append(write)
  }

  for (const link of entries) {
    if (link.url !== 'home.html') {
      loadLinks(link, selector, pre)
    }
  }
}

// FUNCTION TO WRITE LINKS TO SELECT HTML TAGS
function loadLinks(link, selector, pre) {
  // Assemble HTML tag

  if (selector === '.toplinks') {
    write = `<li class='wide'><a href='${pre}/pages/${link.url}'>${link.name}</a></li>`
  }

  if (selector === '.socials') {
    write = `<li><a href='${link.url}' target='_blank' aria-label='${link.name}'>
        <img src='${pre}/${link.image}' alt='${link.name}' width='21' height='21'>
      </a></li>`
  }

  // Render links
  $(selector).append(write)
}

// .................
// STYLING         :
// .................
// .................
// A lot of the styling is done via CSS
// Bits below give the last push
//.........................................


// .................
// BLOG MANAGEMENT
// .................
// .................
// This JSON file IS generated automatically
// That said, the bits below make use of the generated file. They do not generate it.
// ..................................................

// Main function to load blogs
async function blog() {

  // Call function to get filenames (which also has a localhost/GH conditional)
  path = '../json/blog1.json'
  const entries = await getEntries(path)

  // Load each entry & save categories to array
  n = 1
  let cats = 'all'
  for (const blog of entries) {
    await loadBlogEntry(blog, n)
    cats = cats + ' ' + blog.categories
    n = n + 1
  }
  const unique = [...new Set(cats.split(' '))]

  // Paint categories to category bar
  unique.forEach(cat => {
    cat = cat.trim()
    const btn = `<button type="button" onclick="selectCat('${cat}')">${cat}</button>`

    $('#catbar').append(btn)
  })

  // Check if blogs have finished painting to DOM, if not recall function after a few milliseconds
  function check(max) {
    if ($('section').length === entries.length) {
      console.log('all blogs have loaded --> adjusting visuals')
      $('section.invisible').slice(0, 4).removeClass('invisible')
    } else {
      if (max >= 0) {
        console.log('blogs still being painted to DOM. waiting a few milliseconds to adjust visuals')
        setTimeout(function () {
          check(max)
        }, 10)
      }
    }
  }
  var max = 100 // Max number of times to run check. If they haven't loaded by then, there's a different problem
  check(max) // Call function to check if sections have painted
}


// If on blog list, get filenames, headings, and intro for all blog entries
async function getEntries(path) {
  console.log(path)
  // Call JSON file to get info
  const entries = await $.ajax(path)
    .done(function (response) {
    })
    .fail(function () { console.log('error with ajax call') })

  const sorted = entries.sort((a, b) => Date.parse(b.date) - Date.parse(a.date))

  return sorted
}

// After getting filenames for existing blogs, append each blog as <section> on <main>/#blogwrapper
async function loadBlogEntry(blog, n) {
  // Adjust blog info for final render

  const filename = blog.filename
  const cats = blog.categories

  const title = `<h2><a href='../blog/${filename}.html'>${blog.headline}</a></h2>`
  const intro = '<p>' + blog.intro + '</p>'
  const more = `<span class='more'><a href='../blog/${filename}.html'>Read more</a></span>`

  // Prefix for handling events and stuff
  const outer =
    `<section id='${filename}' class='invisible all ${cats}'>
  <div id='blog-${n}' class='internal'></div
  section>`

  $('#blogwrap').append(outer)

  // Render index entry
  // Note! Takes a bit to load. Function will finish before <sections> are painted to DOM
  selector = `#blog-${n}`
  $(selector).html(title + intro + more)
}


// .................
// UX interactions :
// .................
// .................

// NAVBAR 
// Open menu
function openMenu() {
  $('.open').css('display', 'none')
  $('.close').css({ 'display': 'inline-block', 'borderBottom': '0' })
  $('.wide').css('display', 'block')
  $('.socialMenu').css('display', 'none')
}

// Collapse menu
function closeMenu() {
  $('.open').css('display', 'inline-block')
  $('.close').css('display', 'none')
  $('.wide').css('display', 'none')
  $('.socialMenu').css('display', 'inline-block')
}

// BLOG
// Load more blogs
async function loadMoreBlogs() {
  let n = $('section.invisible').length
  if (n !== 0) {
    await $('section.invisible').slice(0, 4).removeClass('invisible')
  }

  n = $('section.invisible').length
  if (n === 0) {
    $('#loadBlogs').addClass('invisible')
  }
}

// Blog's category selection
function selectCat(cat) {
  if (cat === 'all') {
    $('.all').show()
    $('.all:not(.' + cat).show()
  } else {
    $('.all').show()
    $('.all:not(.' + cat).hide()
  }
  let selector = 'section.' + cat
  $('#loadBlogs').addClass('invisible')
}


// MISCELLANOUS STUFF
// Date for copyright
function getFecha() {
  var d = new Date()
  $('#fecha').text(d.getFullYear())
}

// I think this is funny
function iLikeYou() {
  alert('You rebel! I like you!')
  $('.greenButton').css('display', 'none')
}