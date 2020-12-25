const searchFiled=document.querySelector("#searchField");

const tbody=document.querySelector("#tbody");

searchFiled.addEventListener("keyup",(e) =>
{
const searchValue = e.target.value;

if (searchValue.trim().length>0){
tbody.innerHtml="";

fetch("/searchUsers",{
body :JSON.stringify({searchText : searchValue}),

method :"POST",




})
.then((res)=>res.json())

.then((data)=> {
console.log("data",data);


data.forEach((user) => {
     tbody.innerHTML=
 `

         <tr>
             <th scope="row">${user.id}</th>

             <td>${user.first_name}</td>
             <td>${user.last_name}</td>
             <td>${user.email}</td>
             <td>${user.password}</td>


             <td>
                 <a href="edit/${user.id}">Edit</a><span>|</span>
                 <a href="delete/${user.id}">Delete</a>
             </td>


         </tr>

 `
 });

});
}
});