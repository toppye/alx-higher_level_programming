#!/usr/bin/node

//class Rectangle that defines a rectangle
class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}

	print () {
		for (let i = 0; i < this.height; i++){
			let result = 'X'.repeat(this.width);
			console.log(result);
		}
	}
}

module.exports = Rectangle;
