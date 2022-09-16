// Below code can be found at https://docs.agora.io/en/video-legacy/start_call_web?platform=Web
// Relevant adjustments have been made to facilitate integration

// error handling
let handleError = function(err){
    console.log("Error: ", err);
};

// Queries the container to which the remote stream belong.
let remoteContainer = document.getElementById("remote-container");

// adds video streams to the container.
function addVideoStream(elementId){
    // Creates a new div for every stream
    let streamDiv = document.createElement("div");
    // Assigns the elementId to the div.
    streamDiv.id = elementId;
    // Takes care of the lateral inversion
    streamDiv.style.transform = "rotateY(180deg)";
    // Adds the div to the container.
    remoteContainer.appendChild(streamDiv);
};

//removes video stream from the container.
function removeVideoStream(elementId) {
    let remoteDiv = document.getElementById(elementId);
    if (remoteDiv) remoteDiv.parentNode.removeChild(remoteDiv);
};

// Specifing web rtc connection
let client = AgoraRTC.createClient({
    mode: "rtc",
    codec: "vp8",
});

client.init("4e7bcf7bbff741599b6b82ce27663b2d", function() {
    console.log("client initialized");
}, function(err) {
    console.log("client init failed ", err);
});

// Join a channel
// Token  below expires 12/09/22
// need for automated token generation
// allows both audio and video on connection
client.join("007eJxTYBDglrv8/XJqt3AFQ/Um810SJedrTP6FX6v0DpDpv9s2Zb8Cg0mqeVJymnlSUlqauYmhqaVlklmShVFyqpG5mZlxklGKdLRc8qw18smr3+kwMTJAIIjPwpCbmJnHwAAANkMghw==", "main", null, (uid)=>{
    // Create a local stream
    let localStream = AgoraRTC.createStream({
        audio: true,
        video: true,
    });
    // Initializes the local stream
    localStream.init(()=>{
        // Plays the local stream
        localStream.play("zoom_window");
        // Publishes the local stream
        client.publish(localStream, handleError);
    }, handleError);
  }, handleError);

// Subscribes to the remote stream when it is published
client.on("stream-added", function(evt){
    client.subscribe(evt.stream, handleError);
});
// Plays the remote stream when it is subsribed
client.on("stream-subscribed", function(evt){
    let stream = evt.stream;
    let streamId = String(stream.getId());
    addVideoStream(streamId);
    stream.play(streamId);
});

