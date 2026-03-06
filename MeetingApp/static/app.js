document.getElementById('meetingForm').onsubmit = async(e) => {
    e.preventDefault();
    const data = {
        host: document.getElementById('host').value,
        name: document.getElementById('meeting_name').value,
        date_time: document.getElementById('date_time').value
    };

    // Use this for your local Meeting.app backend
    let url = 'http://127.0.0.1:5000/setup_meeting';

    // Use this ONLY if you want to test connectivity with an external site
    // let url = 'https://jsonplaceholder.typicode.com/posts'; 

    const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    const result = await res.json();
    document.getElementById('response').innerText = "Signature: " + result.signature;
};