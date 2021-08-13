

function getId(divId){
    console.log(divId)
    subjectName = document.getElementById(divId).innerText
    console.log(subjectName)
    subject = subjectName.replace(" ", "#")
    
    window.location.href = '/getExamCreate/' + subject ;
}