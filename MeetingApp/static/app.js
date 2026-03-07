document.getElementById('meetingForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
        host: document.getElementById('host').value,
        name: document.getElementById('meeting_name').value,
        date_time: document.getElementById('date_time').value
    };

    try {
        const res = await fetch('/setup_meeting', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await res.json();

        document.getElementById('response').innerText =
            "Signature: " + result.signature;

    } catch (error) {
        console.error("Error:", error);
        document.getElementById('response').innerText =
            "Error creating meeting.";
    }
});