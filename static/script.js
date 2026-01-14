function predictPrice() {

    const data = {
        year: document.getElementById("year").value,
        present_price: document.getElementById("price").value,
        kms: document.getElementById("kms").value,
        fuel: document.getElementById("fuel").value,
        seller: document.getElementById("seller").value,
        transmission: document.getElementById("transmission").value,
        owner: document.getElementById("owner").value
    };

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById("result").innerText =
            "Predicted Price: ₹ " + result.price + " Lakhs";
    });
}
