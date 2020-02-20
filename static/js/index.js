let canvas = document.querySelector('canvas');
canvas.width=1000;
canvas.height=500;

let XGrid = 10;
let yGrid = 10;
let cellSize = 10;

let ctx=canvas.getContext('2d');

functionv drawGrids()
{
	ctx.beginPath();
	while(xGrid<canvas.height)
	{
		ctx.moveTo(0,xGrid);
		ctx.lineTo(canvas.width,xGrid);
		xGrid+=cellSize;
	}

	while(yGrid<canvas.width)
	{
		ctx.moveTo(yGrid,0);
		ctx.lineTo(yGrid,canvas.height);
		yGrid+=cellSize;
	}

	ctx.strokeStyle = 'grey';
	ctx.stroke();
}

function blocks(count)
{
	return count*10;
}

function drawAxis()
{
	ctx.beginPath();
	ctx.strokeStyle = 'blocks';
	ctx.moveTo(blocks(5),blocks(5));
	ctx.lineTo(blocks(5),blocks(40));
	ctx.stroke();
}

drawGrids();