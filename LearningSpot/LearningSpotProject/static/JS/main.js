// create client object - functions as core stream for all funcitonality

let client = AgoraRTC.createClient({mode:"rtc", 'codec':"vp8"}) 


// connect to agora application 'LearningSpot' as created in App Builder
let config = {
    appid:'4e7bcf7bbff741599b6b82ce27663b2d',
    token:'007eJxTYIhKnKTIMDudI93rW1VmSj03G3/9T936tbNbrR68eGX8fKUCg0mqeVJymnlSUlqauYmhqaVlklmShVFyqpG5mZlxklHKZAHWZOEktmTd2kcsjAwQCOKzMOQmZuYxMAAA2S0eGw==', //'main'
    uid:null,
    channel:'main',
}

//localTrack is the abstract interface that defines local audio and video tracks and can be used for playing and publishing audio and video. You can call different methods to create different local track objects based on the derived interfaces of localTrack:

let localTracks = {
    videoTracks:null,
    audioTracks:null,
}

//other users that join the stream
let remoteTracks = {}


//add click event to trigger add join functionality to join button
document.getElementById('join-btn').addEventListener('click', async ()=>{
    console.log('user joined stream')

    await joinStreams()
})


//connect to the agora app
let joinStreams = async () =>{ //async arrow function 

    

    [config.uid, localTracks.audioTracks, localTracks.videoTracks] = await Promise.all([ //passing list after 'Promise; into list before to complete API call//
        client.join(config.appid, config.channel, config.token, config.uid || null), //refers to config and gathers attributes^^//
        AgoraRTC.createMicrophoneAudioTrack(), //allows user to connect audio to stream by populating audioTracks (set to null in localTracks^)
        AgoraRTC.createCameraVideoTrack(), //allows user to connect video to stream by populating videoTracks (set to null in localTracks^)
    ]) 

//create videoPlayer object
    let videoPlayer = `<div class="video-containers" id="video-wrapper-${config.uid}"> 
                                <p class="user-uid"> ${config.uid}</p>
                                <div class="video-player player" id="stream-${config.uid}"></div> 
                        </div>` //use template literals to create video wrapper and adds a unique id from config for each user

//connect to the document and append video player to DOM

    document.getElementById('user-streams').insertAdjacentHTML('beforeend', videoPlayer)
    localTracks.videoTracks.play(`stream-${config.uid}`)

//complete async asyn function ^
    await client.publish([localTracks.audioTracks, localTracks.videoTracks])

    //event listen for remote user joining 
    client.on("user-published", handleUserJoined)
}

let handleUserJoined = async (use, mediaType) => {
    console.log('user has joined stream')
}
