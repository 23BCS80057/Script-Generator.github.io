document.getElementById('script-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const genre = document.getElementById('genre').value.trim();
    const theme = document.getElementById('theme').value.trim();
    const characters = document.getElementById('characters').value.trim().split(',');

    if (!genre || !theme || characters.length === 0) {
    alert('Please fill out all fields!');
    return;
    }

    const scriptText = `
    Title: A ${genre} Tale
    
    Theme: ${theme}
  
    Characters: ${characters.map(name => name.trim()).join(', ')}
  
    Scene 1: The journey begins. ${characters[0]?.trim() || 'Someone'} discovers something unexpected.
    Scene 2: A twist in the story as ${characters[1]?.trim() || 'another character'} faces a challenge.
    Scene 3: ${characters.length > 2 ? characters[2]?.trim() : 'The protagonist'} resolves the conflict, embodying the theme of ${theme.toLowerCase()}.
    `;

    document.getElementById('script-text').textContent = scriptText.trim();
});
