let Name = [];

function addName() {
    const NameInput = document.getElementById("NameInput").value; 
    if (NameInput) {
        Name.push(NameInput);
    }
}
