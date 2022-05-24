document.querySelector("#bee-gone").addEventListener("submit", (e) => {
    e.preventDefault();
    
    const data = new FormData(e.currentTarget)

    const bee = {
        name: data.get("bee-name"),
        id: data.get("bee-id"),
        queen: false
    }
    
    const options = {
        method: 'POST',
        body: JSON.stringify(bee),
        headers: new Headers({
            'Content-Type': 'application/json'
        })
    }

    fetch("http://localhost:3000/bees/new", options)
        .then(r => r.json())
        .then(d => console.log(d))
        .catch(e => console.log("panic", e))


})