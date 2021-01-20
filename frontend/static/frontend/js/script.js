const canvas = document.querySelector("canvas");
const context = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight - 72;

let balls = new Array();
const colors = new Array("red", "yellow", "orange", "green", "pink", "black", "blue", "grey")


window.addEventListener("resize", function() {
    canvas.width = window.innerWidth -100;
    canvas.height = window.innerHeight - 72;
})

class Ball {
    constructor(size, color) {
        this.pos_x = Math.random() * canvas.width;
        this.pos_y = 20;
        this.size = size;
        this.color = color;
        this.x_dir = Math.random();
        this.y_dir = Math.random() * 10;

        if (this.y_dir < 5){
            this.y_dir += Math.random() * 5;
        }
    }

    move() {
        if (this.pos_x >= canvas.width || this.pos_x <= 0) {
            this.x_dir *= -1;
        }
        if (this.pos_y >= canvas.height || this.pos_y <= 0) {
            this.y_dir *= -1;
            this.size = Math.ceil(this.size / 4);
        }
        this.pos_y += this.y_dir
    }

    draw() {
        context.beginPath();
        if (this.size >= 2) {
            context.arc(this.pos_x, this.pos_y, this.size, 0, Math.abs(2 * Math.PI));
            context.fillStyle = this.color;
            context.fill();
            context.stroke();
        }
    }
}


function ballDraw() {
    balls = balls.filter(ball => ball.size > 1)
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = "black";

    fontsize = canvas.width * 0.07
    font = fontsize + "px san-serif"
    context.font = font    

    const id = document.querySelector("canvas").id
    
    let text = "Current work in progress"
    if (canvas.id == "canvas-progress") {
        text = "Work in Progress";
    } else {
        text = "Something went wrong!"
    }

    let textWidth = context.measureText(text).width;
    let textHeight = context.measureText(text);
    context.fillText(text, (canvas.width / 2) - (textWidth / 2), (canvas.height / 2) - (textHeight.actualBoundingBoxAscent / 4));


    if (balls.length < 20) {
        balls.forEach(function(obj) {
            obj.draw();
            obj.move();
        })
    }
}

setInterval(function() {
    index = Math.round(Math.random() * colors.length)
    balls.push(new Ball(Math.random() * 20, colors[index]));
}, 1000)

setInterval(ballDraw, 10)