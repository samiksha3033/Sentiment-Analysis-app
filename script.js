function analyzeSentiment() {
    const text = document.getElementById("userText").value;

    // prevent empty input
    if(text.trim() === "") {
        alert("Please enter some text!");
        return;
    }

    fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"   // 🔑 must
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {

        if (data.error){
        alert(data.error);
        return;
        }
        // Fill result page
        document.getElementById("resultText").innerText = data.text;
        document.getElementById("resultSentiment").innerText = data.sentiment;
        document.getElementById("resultConfidence").innerText = data.confidence;
        document.getElementById("resultScore").innerText = data.score;

        // Switch pages
        document.getElementById("inputPage").style.display = "none";
        document.getElementById("resultPage").style.display = "block";
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Something went wrong, please try again.");
    });
}

function goBack() {
    document.getElementById("resultPage").style.display = "none";
    document.getElementById("inputPage").style.display = "block";
    document.getElementById("userText").value = ""; // clear textarea
}
