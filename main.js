document.getElementById('startButton').addEventListener('click', () => {
  // Generate a unique meeting ID
  const meetingId = Math.random().toString(36).substr(2, 9);
  // Redirect to the meeting page with the meeting ID
  window.location.href = `meeting.html?meetingId=${meetingId}`;
});

document.getElementById('joinButton').addEventListener('click', () => {
  const meetingId = document.getElementById('meetingIdInput').value.trim();
  if (meetingId) {
    window.location.href = `meeting.html?meetingId=${meetingId}`;
  } else {
    alert('Please enter a valid Meeting ID.');
  }
});
