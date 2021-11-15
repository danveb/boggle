$(function() {

    // initialize class
    class Boggle {
        constructor(boardId) {
            console.log('reading'); 
            this.score = 0 
            this.words = new Set()
            this.board = $('#', boardId)
            $('.check-word').on('submit', this.handleClick.bind(this))
            $('#boggle').append(`<p id="currentscore">Current score: ${this.score}</p>`)
            // timer for 60 seconds
            setTimeout(this.scoreIt.bind(this), 60000)
        }

        // handleClick event
        async handleClick(e) {
            e.preventDefault()
            const $word = $('#guess')
            const guess = $word.val() 
            // check if guess is inside words Set
            if(this.words.has(guess)) {
                // found it! so we just return 
                alert(`Already found ${guess}`, 'ok')
                return
            }
            const response = await axios.get('/check', {params: {'guess': guess}})
            console.log(response)
            // console.log(response.data) // result: 'ok' 
            // check if response is "result": "ok" 
            if(response.data.result === 'ok') {
                // increase score 
                this.score += guess.length 
                this.words.add(guess)
                // display score 
                $('#currentscore').html(`<p id="currentscore">Current score: ${this.score}</p>`)
            } else if(response.data.result === 'not-on-board') {
                alert(`${guess} is not on this board.`)
            } else {
                alert(`${guess} is not a valid English word.`)
            }
        }

        async scoreIt() {
            console.log('score!');
            // hide guessing input and submit buttons 
            $('#guess').hide()
            $('.btn-submit').hide()
            const response = await axios.post('/score', { 'score': this.score })
            if(response.data.newRecord) {
                alert(`New record: ${this.score}`, 'ok')
            } else {
                alert(`Final score: ${this.score}`, 'ok')
            }
        }
    }

    // instantiate new Boggle game
    let game = new Boggle('boggle')

}); 