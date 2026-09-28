const form = document.getElementById("predictionForm");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const data = {
        Car_Age: Number(document.getElementById("Car_Age").value),
        Kilometers_Driven: Number(document.getElementById("Kilometers_Driven").value),
        Engine_Capacity: Number(document.getElementById("Engine_Capacity").value),
        Mileage: Number(document.getElementById("Mileage").value),
        Previous_Owners: Number(document.getElementById("Previous_Owners").value),
        Fuel_Type: document.getElementById("Fuel_Type").value,
        Transmission: document.getElementById("Transmission").value,
        Car_Brand: document.getElementById("Car_Brand").value
    };

    const resultMessage = document.getElementById("resultMessage");
    const predictedPrice = document.getElementById("predictedPrice");

    resultMessage.textContent = "Calculating price...";

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }
        );

        const result = await response.json();

        if (!response.ok) {
            throw new Error("Prediction failed");
        }

        predictedPrice.textContent =
            "₹ " + Number(result.predicted_price).toLocaleString("en-IN");

        resultMessage.textContent =
            "Estimated price generated successfully!";

    } catch (error) {

        predictedPrice.textContent = "₹ 0";

        resultMessage.textContent =
            "Unable to connect to the prediction server.";

        console.error(error);
    }

});