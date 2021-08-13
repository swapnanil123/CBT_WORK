
url = $(location).attr('href');
// console.log(url)
splitUrl = url.split('/')
const subject= splitUrl[splitUrl.length - 1].replace("#", " ")
console.log(subject)

$("#head").text(subject)