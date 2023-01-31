const { spawn } = require("child_process");

document.getElementById("transfer").addEventListener("click", function() {
    const input = document.getElementById("link").value;
    const pyprog = spawn("python", ["src/Backend/Spotify_to_YouTube/run.py", input]);

    pyprog.stdout.on("data", function(data) {});
    console.log(data.toString());
});