function reset(){
    document.getElementById("form").reset()
    document.getElementById("bookId").value = ""
}
var bookList2=[]
var bookList = []
function save(){
    let read = document.getElementById("bookComplete")
    if(read.checked == true){
        //alert('READ')
       bookList = JSON.parse(localStorage.getItem('listItem3')) ?? []
        var id 
        bookList.length != 0 ? bookList.findLast((item)=> id = item.id) : id = 0
        
        if(document.getElementById('bookId').value){
            bookList.forEach(value => {
                if(document.getElementById('bookId').value == value.id){
                    value.title = document.getElementById('bookTitle').value,
                    value.author = document.getElementById('bookAuthor').value,
                    value.year = document.getElementById('bookYear').value,
                    value.isComplete = 1
                }
            })
        }
        else{
            var item = {
                id : id +1,
                title:document.getElementById('bookTitle').value,
                author:document.getElementById('bookAuthor').value,
                year:document.getElementById('bookYear').value,
                isComplete:1
            }
            bookList.push(item)
        }
        localStorage.setItem('listItem3', JSON.stringify(bookList))
    }
    //When the checkbox is not checked
    else{
        //var booklist2 = []
        bookList2 = JSON.parse(localStorage.getItem('listItem4')) ?? []
        var id
        bookList2.length !=0 ? bookList.findLast((item) => id=item.id): id = 0
        if(document.getElementById('bookId').value){
            bookList2.forEach(value=>{
                if(document.getElementById('bookId').value == value.id){
                    value.title = document.getElementById('bookTitle').value
                    value.author = document.getElementById('bookAuthor').value
                    value.year = document.getElementById('bookYear').value
                    value.isComplete = 0
                }
            })
            document.getElementById('bookId').value=''
        }
        else{
            var item = {
                id:id+1,
                title:document.getElementById('bookTitle').value,
                author:document.getElementById('bookAuthor').value,
                year:document.getElementById('bookYear').value,
                isComplete:0
            }
            bookList2.push(item)
        }
        localStorage.setItem('listItem4', JSON.stringify(bookList2))
    }
    showData()
    document.getElementById('form').reset()
}

function showData(){
    let table = document.getElementById('dataTable')
    table.innerHTML=``
    bookList = JSON.parse(localStorage.getItem('listItem4')) ?? []
    bookList.forEach((value, i) =>{
        table.innerHTML += `
        <tr>
            <td>${i+1}</td>
            <td>${value.title}</td>
            <td>${value.author}</td>
            <td>${value.year}</td>
            <td><button class="btn btn-sm btn-warning" >Read</button></td>
            <td><button class="btn btn-sm btn-success" >Edit</button></td>
            <td><button class="btn btn-sm btn-danger" >Delete</button></td>
         </tr>   `
    })
    let table2 = document.getElementById('dataTable2')
    table2.innerHTML=``
    bookList2 = JSON.parse(localStorage.getItem('itemList3')) ?? []
    bookList2.forEach((value2, i) =>{
        table2.innerHTML += `
        <tr>
            <td>${i+1}</td>
            <td>${value2.title}</td>
            <td>${value2.author}</td>
            <td>${value2.year}</td>
            <td><button class="btn btn-sm btn-warning" >Read</button></td>
            <td><button class="btn btn-sm btn-success" >Edit</button></td>
            <td><button class="btn btn-sm btn-danger" >Delete</button></td>
         </tr>   `
    })
}