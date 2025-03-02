# بسم الله الرحمن الرحيم
# الحمد لله وحده، والصلاة والسلام على من لا نبي بعده ﷺ

# Introduction to HTML5 Canvas

HTML5 Canvas is a powerful 2D drawing API that allows you to draw shapes, text, images, and more directly in the browser using JavaScript. This tutorial will walk you through everything you need to get started with Canvas — from setting up a simple canvas on a webpage to creating complex drawings, animations, and even simple games.

## 1. Setting Up the Canvas

Before drawing anything, you need to add a `<canvas>` element to your HTML and get its drawing context in JavaScript:

```html
<!-- HTML: Define a canvas with an id and optional width/height -->
<canvas id="myCanvas" width="500" height="400">
  Your browser does not support the <code>&lt;canvas&gt;</code> element.
</canvas>
```

In HTML, the canvas tag creates a blank drawing surface. The `width` and `height` set the canvas size in pixels (default is 300×150 if not specified ([Canvas tutorial - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial#:~:text=major%20browsers,creates%20graphics%20on%20the%20fly))). The content between `<canvas>...</canvas>` is fallback text for older browsers.

Next, obtain the **2D rendering context** in JavaScript, which provides the drawing methods:

```js
// JavaScript: Getting the canvas element and context
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");  // "2d" for 2D rendering context
```

Calling `getContext("2d")` on the canvas gives you a **CanvasRenderingContext2D** object, here stored in `ctx`, which is what you'll use to draw. Always ensure the canvas element exists in the DOM before calling `getContext`.

### Canvas Coordinate System

Canvas uses a **pixel-based coordinate system**. The **origin (0,0)** is at the top-left corner of the canvas ([HTML Canvas Coordinates](https://www.w3schools.com/graphics/canvas_coordinates.asp#:~:text=The%20HTML%20canvas%20is%20a,dimensional%20grid)). The X axis increases to the right, and the Y axis increases downward (i.e., pixels below the top have greater Y values). For example, a point at (100, 50) is 100 pixels from the left edge and 50 pixels from the top edge.

All drawing operations use this coordinate grid. By default, one grid unit equals one pixel ([Drawing shapes with canvas - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes#:~:text=Before%20we%20can%20start%20drawing%2C,wide%20and%20150%20pixels%20high)). You can change the coordinate system by applying transformations (as we'll see later), but initially it's a simple Cartesian grid with the top-left as (0,0). 

## 2. Basic Drawing Operations

The canvas context (`ctx`) provides several methods to draw basic shapes and paths.

### Drawing Rectangles

Canvas supports basic rectangles with dedicated methods:

- `ctx.fillRect(x, y, width, height)` – Draws a **filled** rectangle ([Drawing shapes with canvas - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes#:~:text=fillRect)).
- `ctx.strokeRect(x, y, width, height)` – Draws a rectangle **outline** (stroke only) ([Drawing shapes with canvas - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes#:~:text=fillRect)).
- `ctx.clearRect(x, y, width, height)` – Clears the specified rectangular area, making it fully transparent (useful for erasing) ([Drawing shapes with canvas - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes#:~:text=strokeRect)).

All these methods use the same parameters: (x, y) for the top-left corner and the rectangle's width and height in pixels ([Drawing shapes with canvas - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes#:~:text=Each%20of%20these%20three%20functions,provide%20the%20rectangle%27s%20size)).

**Example – Drawing and Clearing Rectangles:**

```js
// Set a fill color and draw a filled rectangle
ctx.fillStyle = "steelblue";            // set fill color
ctx.fillRect(25, 25, 100, 100);         // filled square at (25,25) with 100px sides

// Clear a 60x60 area inside it (making a "hole")
ctx.clearRect(45, 45, 60, 60);          // clear a smaller square inside

// Set a stroke style and draw rectangle outline
ctx.strokeStyle = "black";             // outline color
ctx.lineWidth = 5;                     // line width for outline
ctx.strokeRect(50, 50, 50, 50);        // draw outlined square inside the cleared area
```

In this code, we first draw a steel blue square. Then `clearRect` erases a smaller square from its center, and finally `strokeRect` draws a black border square. The end result is a blue square with a hollow center and a black outline around the hollow part. This matches the behavior described in the MDN example: *“The `fillRect()` draws a filled square, `clearRect()` erases a 60×60 area from the center, and `strokeRect()` creates a 50×50 outline inside the cleared square.”* ([Drawing shapes with canvas - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes#:~:text=The%20,pixels%20within%20the%20cleared%20square))

### Drawing Paths (Lines and Shapes)

For shapes other than rectangles, you will use **paths**. Drawing a path in canvas involves the following steps ([Drawing shapes with canvas - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes#:~:text=Drawing%20paths)):

1. **Begin a path:** `ctx.beginPath()` – resets the current path, starting fresh.
2. **Define path points:** Use drawing commands like `moveTo`, `lineTo`, `arc`, etc., to draw segments.
3. **Render the path:** call `ctx.fill()` to fill the shape or `ctx.stroke()` to outline the path.

Some common path drawing commands:

- `ctx.moveTo(x, y)` – Move the drawing cursor (pen) to a specific coordinate without drawing. Use this for the starting point of a shape.
- `ctx.lineTo(x, y)` – Draw a line from the current cursor position to the given (x, y) coordinate.
- `ctx.arc(x, y, radius, startAngle, endAngle, counterclockwise)` – Draw an arc or circle centered at (x, y). Angles are in radians (for reference, 360° = 2π radians).
- `ctx.closePath()` – (Optional) Closes the path by drawing a straight line from the last point back to the starting point. Not strictly required before filling or stroking, but useful for shapes.

**Example – Drawing Lines and a Triangle:**

```js
ctx.beginPath();          // start a new path
ctx.moveTo(50, 50);       // start at (50,50)
ctx.lineTo(150, 50);      // draw line to (150,50)
ctx.lineTo(150, 150);     // draw line to (150,150)
ctx.lineTo(50, 150);      // draw line to (50,150)
// At this point we've defined a rectangle path from (50,50) through (150,150)
// Optionally, close the path (will connect back to starting point)
ctx.closePath();
ctx.strokeStyle = "green";
ctx.stroke();             // draw the outline of the path in green
```

The above will draw an outlined rectangle. We could also fill it by using `ctx.fillStyle = color` and `ctx.fill()` instead of stroke. 

**Example – Drawing a Circle:**

```js
ctx.beginPath();
ctx.arc(200, 75, 50, 0, Math.PI * 2, false); // circle centered at (200,75) with radius 50
ctx.fillStyle = "orange";
ctx.fill();    // fill the circle with orange color
```

Here `arc(x, y, radius, 0, 2π)` draws a full circle. We set a fill style and call `fill()` to draw a filled circle. If we wanted just an outline, we could call `ctx.stroke()` instead after setting `ctx.strokeStyle`. 

**Tip:** When drawing multiple separate shapes on one canvas, call `beginPath()` before each shape to prevent unintended connections between paths. Also, `fillRect` and `strokeRect` automatically draw immediately, so you don't use them inside a `beginPath`/`stroke` sequence (they are separate convenience methods).

### Colors and Styles

By default, shapes are drawn in solid black. You can change colors using:

- `ctx.fillStyle = "color"` – sets the fill color for shapes.
- `ctx.strokeStyle = "color"` – sets the stroke (outline) color ([Applying styles and colors - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Applying_styles_and_colors#:~:text=)).
- `ctx.lineWidth = value` – sets the width of stroke lines (default is 1px).

You can specify colors by name (`"red"`), hex code (`"#FF0000"`), RGB/RGBA (`"rgb(255,0,0)"`, or `"rgba(255,0,0,0.5)"` for 50% transparency), HSL, etc., just like in CSS. Once set, the style remains in effect for subsequent drawing calls until changed. 

**Example – Using Colors:**

```js
ctx.fillStyle = "#3498db";          // a blue color
ctx.strokeStyle = "rgb(200, 0, 0)"; // red outline
ctx.lineWidth = 4;

ctx.beginPath();
ctx.moveTo(300, 20);
ctx.lineTo(380, 80);
ctx.lineTo(300, 140);
ctx.closePath();
ctx.fill();    // fills the triangle with ctx.fillStyle (blue)
ctx.stroke();  // outlines the triangle with ctx.strokeStyle (red), 4px thick
```

In this example, a triangle is drawn filled with blue and outlined in red. Note that we set the styles *before* calling `fill()` or `stroke()`, so they apply to this path.

### Gradients and Patterns

Canvas allows you to use gradients or image patterns as fill or stroke style:

- **Linear Gradient:** Create with `ctx.createLinearGradient(x1, y1, x2, y2)`, then add color stops. For example:

  ```js
  const grad = ctx.createLinearGradient(0, 0, 150, 0); // horizontal gradient
  grad.addColorStop(0, "magenta");
  grad.addColorStop(0.5, "blue");
  grad.addColorStop(1, "red");
  ctx.fillStyle = grad;
  ctx.fillRect(10, 10, 150, 100); // fill rectangle with gradient
  ```

  Here we created a gradient from x=0 to x=150 and added three colors. The rectangle will blend from magenta to blue to red horizontally.

- **Radial Gradient:** Use `ctx.createRadialGradient(x1, y1, r1, x2, y2, r2)` similarly (with inner and outer circle).

- **Pattern:** Use `ctx.createPattern(image, repeatMode)` to fill with a repeating image (where `repeatMode` can be `"repeat"`, `"no-repeat"`, etc.).

Just assign the gradient or pattern to `fillStyle` or `strokeStyle`. Both gradient and pattern produce a `CanvasPaint` object that the context can use for rendering.

We'll see an example with images in a later section.

## 3. Text Rendering

Canvas can render text with the current fill or stroke style. Key properties and methods for text are:

- `ctx.font` – specifies font size and family, just like CSS (default `"10px sans-serif"` ([HTML Canvas Text](https://www.w3schools.com/graphics/canvas_text.asp#:~:text=The%20,the%20size%20of%20the%20font))).
- `ctx.textAlign` – horizontal alignment of text relative to given point: `"start"`, `"end"`, `"left"`, `"right"`, or `"center"` (default is `"start"` which is left-aligned for left-to-right languages).
- `ctx.textBaseline` – vertical alignment relative to the given Y: `"top"`, `"middle"`, `"bottom"`, `"alphabetic"` (default), etc. 
- `ctx.fillText(text, x, y)` – fill a text string at (x, y) position ([HTML Canvas Text](https://www.w3schools.com/graphics/canvas_text.asp#:~:text=%2A%20%60fillText%28%29%60%20,text%20%28no%20fill)).
- `ctx.strokeText(text, x, y)` – stroke (outline) the text at (x, y) ([HTML Canvas Text](https://www.w3schools.com/graphics/canvas_text.asp#:~:text=%2A%20%60fillText%28%29%60%20,text%20%28no%20fill)).
- `ctx.measureText(text)` – returns a `TextMetrics` object with properties like `.width` for the width of the given text in the current font ([Drawing text - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_text#:~:text=measureText)).

**Example – Drawing Text:**

```js
ctx.font = "20px Arial";             // set font size and family
ctx.fillStyle = "black";
ctx.fillText("Hello Canvas", 50, 50); // draw filled text at (50,50) ([HTML Canvas Text](https://www.w3schools.com/graphics/canvas_text.asp#:~:text=ctx.fillText%28))

ctx.strokeStyle = "blue";
ctx.lineWidth = 2;
ctx.strokeText("Outline Text", 50, 80); // draw outlined text at (50,80)
```

This will write "Hello Canvas" in black 20px Arial, and below it "Outline Text" with a blue outline.

By default, the x,y position in `fillText`/`strokeText` is the **bottom-left** of the text string (because `textBaseline` defaults to `"alphabetic"` and `textAlign` defaults to `"start"` which for left-to-right is left). You can adjust alignment:

```js
ctx.textAlign = "center";
ctx.textBaseline = "middle";
ctx.fillText("Centered Text", canvas.width/2, canvas.height/2);
```

The above will draw the text centered both horizontally and vertically at the canvas center. This is useful for placing titles or labels.

To measure text width (for example, to underline text or to align another element next to the text), use `ctx.measureText()`:

```js
const metrics = ctx.measureText("Hello Canvas");
console.log(metrics.width);  // logs the width of the text in pixels ([Drawing text - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_text#:~:text=measureText))
```

The `TextMetrics.width` gives the advance width of the text in the current font. Note that canvas text rendering doesn’t provide direct line-breaking or multiline support; you'd have to handle newlines manually (e.g., by splitting text and increasing y for each line).

## 4. Transformations and State

Canvas supports **transformations** that let you translate (move), rotate, and scale the coordinate system itself. Instead of moving every shape's coordinates, you can transform the canvas grid, and then draw as normal.

### Translate, Rotate, Scale

- `ctx.translate(x, y)` – Moves the origin of the canvas by (x, y) pixels. After translating, all drawing commands are offset by that translation.
- `ctx.rotate(angle)` – Rotates the canvas coordinate system by `angle` radians around the current origin. Positive angles rotate clockwise by default ([HTML Canvas Transformations](https://www.w3schools.com/graphics/canvas_transformations.asp#:~:text=%2A%20%60rotate%28%29%60%20,transformation%20with%20the%20arguments%20described)). (To rotate in degrees, convert degrees to radians: radians = degrees * Math.PI/180).
- `ctx.scale(sx, sy)` – Scales the grid by sx horizontally and sy vertically (e.g., scale(2,2) makes everything drawn twice as large in each dimension; scale(1,-1) would flip vertically).

**Example – Using Translate and Rotate:**

```js
// Draw a rectangle normally
ctx.fillStyle = "purple";
ctx.fillRect(20, 20, 60, 30);  // draws at (20,20)

// Move the origin and draw the same rectangle
ctx.translate(100, 50);       // shift origin by (100,50)
ctx.fillRect(20, 20, 60, 30);  // this rectangle is actually at (120,70) in the original coordinates

// Rotate the canvas 45 degrees (around the new origin at (100,50))
ctx.rotate((45 * Math.PI) / 180);  // 45 degrees in radians
ctx.fillStyle = "orange";
ctx.fillRect(20, 20, 60, 30);  // this rectangle is rotated 45° relative to the previous origin
```

In this snippet:
- We first draw a purple rectangle at (20,20).
- Then we translate the canvas by (100,50). Now coordinate (0,0) is effectively where (100,50) used to be. A subsequent fillRect(20,20,...) draws relative to the translated origin (so effectively at original (120,70)).
- Then we rotate the canvas by 45°. Further drawing is rotated. The orange rectangle appears rotated because the canvas axes themselves have been rotated.

**Important:** Transforms are cumulative. The translate affected the origin for the rotate as well. The order of operations matters (rotate then translate is different from translate then rotate).

If you ever need to reset transformations, you can use the canvas **save and restore state**.

### Saving and Restoring State

The canvas context maintains a stack of drawing states. A state includes transformations, styles (colors, line widths), and other settings. You can save the current state with `ctx.save()` and restore the last saved state with `ctx.restore()`.

- `ctx.save()` – Pushes the current state onto a stack.
- `ctx.restore()` – Pops the top state from the stack and restores it.

Use these around transformations to isolate their effect:

```js
ctx.save();
ctx.translate(100, 0);
ctx.rotate(Math.PI/4);
// draw some rotated stuff
ctx.restore();  // back to original state (no translate/rotate)
// draw more, unaffected by the prior transform
```

After restoring, the coordinate system and styles revert to what they were at the last save. This is much easier than manually undoing transformations.

Always pair each `save()` with a corresponding `restore()`. You can call save/restore multiple times (they nest like push/pop). This is extremely useful in animations and complex drawings where you temporarily change the coordinate system or styles and then want to go back quickly.

## 5. Working with Images

One of the powerful features of canvas is drawing and manipulating images.

### Loading and Drawing Images

To draw an image onto the canvas, you typically:

1. Create an `Image` object (or use an existing `<img>` element).
2. Set its `src` to the image URL.
3. Draw it in the canvas once it's loaded (e.g., in the `onload` handler).

The primary method is `ctx.drawImage()` which can draw an image (or another canvas) onto your canvas. It has three forms:

- `ctx.drawImage(image, dx, dy)` – Draw the image at the position (dx, dy) on the canvas (top-left of image at that coordinate).
- `ctx.drawImage(image, dx, dy, dWidth, dHeight)` – Draw the image at (dx, dy) and **scale** it to the specified width and height (dWidth, dHeight).
- `ctx.drawImage(image, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight)` – Draw a **sub-rectangle** of the source image (crop from sx,sy with size sWidth×sHeight) at (dx, dy) on canvas, and scale it to dWidth×dHeight.

**Example – Basic Image Drawing:**

```js
const img = new Image();
img.onload = function() {
  // draw the image at (10, 10) at its natural size
  ctx.drawImage(img, 10, 10);
};
img.src = "picture.png";
```

When the image loads, it will be drawn onto the canvas at coordinate (10,10). This uses the first syntax of `drawImage`.

**Example – Cropping and Scaling an Image:**

```js
// Assume img is already loaded (or use in onload as above)
ctx.drawImage(
  img,
  50, 50, 100, 100,   // source rect: crop 100x100 area from (50,50) on the image
  200, 200, 100, 100  // destination: draw at (200,200) on canvas, size 100x100
);
```

This takes a 100×100 region from the source image (at source image coords 50,50) and draws that region at (200,200) on the canvas at 100×100 size (in this case, same size, so just cropping without scaling).

Using the third form of `drawImage`, you can do sprite animations (drawing one frame from a sprite sheet at a time) or thumbnail generation (drawing a scaled down portion of an image).

### Image Manipulation and Effects

Canvas also allows pixel-level operations and filtering:

- **Global Composite Operations:** You can draw images (or shapes) with different blending modes by setting `ctx.globalCompositeOperation` (e.g., `"source-over"` (default), `"destination-over"`, `"multiply"`, etc.). This determines how new drawing is combined with existing canvas content. For example, drawing with `globalCompositeOperation = "destination-over"` will put new shapes *behind* the existing ones.

- **Global Alpha:** You can set `ctx.globalAlpha = 0.5` to make all subsequent drawing 50% transparent (until you change it back to 1.0).

- **Image Filters:** Modern Canvas API supports a `ctx.filter` property (similar to CSS filters) for effects like blur, grayscale, etc. For instance, `ctx.filter = "blur(5px) contrast(200%)"; ctx.drawImage(img, 0, 0);` would draw a blurred, high-contrast version of the image. Remember to reset `ctx.filter = "none"` after if you want normal drawing again.

- **Pixel Manipulation:** You can directly access pixel data with `ctx.getImageData(x, y, width, height)`, which returns an `ImageData` object containing an array of pixel values (RGBA). You can iterate over `imageData.data` array (which contains bytes [0–255] for R, G, B, A for each pixel) and manipulate it. For example, to invert colors or to convert to grayscale by averaging channels ([Pixel manipulation with canvas - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Pixel_manipulation_with_canvas#:~:text=data%5Bi%5D%20%3D%20255%20,%2F%2F%20blue)). After modifying pixel data, you put it back with `ctx.putImageData(imageData, dx, dy)`.

**Example – Simple Grayscale Conversion:**

```js
// Get pixel data of the entire canvas
const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
const data = imageData.data;
for (let i = 0; i < data.length; i += 4) {
  const r = data[i], g = data[i+1], b = data[i+2];
  const avg = (r + g + b) / 3;
  data[i] = data[i+1] = data[i+2] = avg;  // set red, green, blue to average
  // alpha (data[i+3]) remains the same
}
ctx.putImageData(imageData, 0, 0);
```

This code takes the canvas image data and converts it to grayscale by setting each pixel's R, G, B to their average value. This kind of direct pixel manipulation is powerful but can be slower for large images, so use it only if needed (like implementing custom filters or effects that aren't available via `ctx.filter`).

## 6. Animations with Canvas

Canvas is great for creating animations and games. Since Canvas itself is just a bitmap, animations are done by *redrawing* the scene for each frame. There are two common ways to create a loop: using `setInterval/setTimeout` or the modern **`requestAnimationFrame`** API, which is preferred for smooth 60fps animations in sync with the browser's refresh.

### Using `requestAnimationFrame`

`window.requestAnimationFrame(callback)` tells the browser you want to perform an animation and should call the `callback` to update the canvas *just before the next repaint*. This results in smoother animations and better CPU efficiency than a manual timer.

**Basic Animation Loop Example:**

```js
let x = 0;
function drawFrame() {
  ctx.clearRect(0, 0, canvas.width, canvas.height); // clear previous frame ([Advanced animations - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Advanced_animations#:~:text=ctx,vy))
  
  // Draw a moving square
  ctx.fillStyle = "red";
  ctx.fillRect(x, 100, 50, 50);
  
  // Update position for next frame
  x += 2;
  if (x > canvas.width) {
    x = -50; // reset square to start from left again (looping)
  }
  
  requestAnimationFrame(drawFrame); // schedule next frame
}
drawFrame(); // start the animation
```

Here, `drawFrame` clears the canvas, draws a red square at the current `x` position, updates `x`, and then schedules itself to run again. The result is a red square moving across the canvas repeatedly. We used `clearRect` to wipe the whole canvas each frame so the moving square doesn't leave a trail.

Using `requestAnimationFrame` automatically tries to run ~60 times per second (can vary based on display refresh rate), and it will pause when the tab is in background, saving resources.

### Sprite-Based Animations

For animations with images (sprites), the concept is similar: have a sprite sheet (one image containing multiple frames) or multiple image frames, and draw one frame per animation tick.

For example, if you have a sprite sheet with frames in a row, you can use `drawImage` with the source rectangle parameters to draw a specific frame:

```js
let frameIndex = 0;
const frameWidth = 64, frameHeight = 64;
const numFrames = 4;
function animateSprite() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // calculate source x based on frame index
  const sx = frameIndex * frameWidth;
  ctx.drawImage(spriteImg, sx, 0, frameWidth, frameHeight, 100, 100, frameWidth, frameHeight);
  
  frameIndex = (frameIndex + 1) % numFrames; // loop frame index
  requestAnimationFrame(animateSprite);
}
animateSprite();
```

If `spriteImg` contains 4 frames of 64×64 next to each other in one row, this will cycle through frames 0,1,2,3 and back to 0, giving an animation. Adjust timing if needed (you could update frameIndex every few calls to slow the animation).

### Bouncing Ball Example

Let's implement a classic bouncing ball, which demonstrates movement, basic physics, and collision with canvas bounds:

```js
let bx = 50, by = 50;       // ball position
let vx = 2, vy = 3;         // ball velocity in x and y
const radius = 20;

function updateBall() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw the ball
  ctx.beginPath();
  ctx.arc(bx, by, radius, 0, Math.PI * 2);
  ctx.fillStyle = "cornflowerblue";
  ctx.fill();

  // Update position
  bx += vx;
  by += vy;

  // Bounce off walls by reversing velocity when hitting edges
  if ((bx + radius > canvas.width) || (bx - radius < 0)) {
    vx = -vx;  // reverse horizontal direction
  }
  if ((by + radius > canvas.height) || (by - radius < 0)) {
    vy = -vy;  // reverse vertical direction
  }

  requestAnimationFrame(updateBall);
}
updateBall();
```

This will create a blue ball that moves and bounces off the edges of the canvas. The checks ensure that if the ball is about to go out of bounds (right or left edge for x, bottom or top for y), we invert the velocity in that direction to make it "bounce" back into the canvas.

The movement appears smooth because of `requestAnimationFrame`, and the physics here is very simple (perfectly elastic collision with walls).

## 7. User Interaction and Events

Canvas itself doesn’t have built-in event handling for shapes — it's just a bitmap. However, the canvas element *can* capture DOM events like mouse clicks, movement, or touch events. You can use normal DOM event listeners on the canvas and then calculate if those events correspond to certain drawn shapes.

Common interactions:
- **Mouse**: click, move, drag on canvas.
- **Keyboard**: key presses for game control or drawing.
- **Touch**: (similar to mouse, using touch events for mobile).

### Mouse Events on Canvas

You can add event listeners to the canvas element for events such as `"mousedown"`, `"mouseup"`, `"mousemove"`, `"click"`, etc. For example:

```js
canvas.addEventListener("mousedown", function(e) {
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  console.log("Canvas clicked at ", x, y);
});
```

Here we compute the mouse position relative to the canvas by adjusting for the canvas's bounding rectangle (this handles page scrolling or if the canvas is not at the very top). Many browsers also provide `e.offsetX` and `e.offsetY` which give the mouse position relative to the event target (which is the canvas in this case), simplifying this calculation.

**Example – Simple Drawing (Painting) with Mouse:**

Let's make a simple paint brush that draws as you drag the mouse:

```js
let painting = false;
canvas.onmousedown = () => { painting = true; ctx.beginPath(); };
canvas.onmouseup = () => { painting = false; };
canvas.onmousemove = e => {
  if (!painting) return;
  // get mouse position relative to canvas
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  // draw a small circle at the mouse position
  ctx.fillStyle = "black";
  ctx.beginPath();
  ctx.arc(x, y, 2, 0, Math.PI * 2);
  ctx.fill();
};
```

This code sets a flag `painting` when the mouse is pressed, and stops painting when released. On mousemove, if painting is true, it draws a tiny circle (radius 2) at the mouse location. Moving the mouse while holding the button will produce a continuous line of circles, which looks like drawing. We call `beginPath()` on mousedown to start a fresh path in case we later want to connect strokes; but here we are just filling individual dots.

For more advanced painting, one might use `ctx.lineTo` as the mouse moves, to draw a continuous stroke. For example, you could do:

```js
canvas.onmousedown = e => {
  painting = true;
  ctx.beginPath();
  ctx.moveTo(getX(e), getY(e));
};
canvas.onmousemove = e => {
  if (painting) {
    ctx.lineTo(getX(e), getY(e));
    ctx.stroke();
  }
};
```

Where `getX(e)` and `getY(e)` compute relative positions. This draws a continuous line following the mouse.

### Drag and Drop (Moving Shapes)

To drag shapes drawn on canvas, you have to implement hit detection manually: check if a mouse down event is within the bounds of a shape you have drawn, then on mousemove update that shape’s coordinates, and redraw the scene.

**Example – Draggable Rectangle:**

Suppose we drew a rectangle and want to let the user drag it:

```js
let rectX = 50, rectY = 50, rectW = 100, rectH = 80;
let dragging = false;

canvas.onmousedown = e => {
  const x = e.offsetX, y = e.offsetY;
  // Hit test: check if (x,y) is inside the rectangle
  if (x > rectX && x < rectX + rectW && y > rectY && y < rectY + rectH) {
    dragging = true;
  }
};
canvas.onmouseup = () => { dragging = false; };
canvas.onmousemove = e => {
  if (dragging) {
    // Move rectangle so that its center follows mouse (or you could offset by click point)
    rectX = e.offsetX - rectW / 2;
    rectY = e.offsetY - rectH / 2;
    // Redraw canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "skyblue";
    ctx.fillRect(rectX, rectY, rectW, rectH);
  }
};
```

This code checks on mousedown if the click is inside our rectangle’s area. If yes, set `dragging`. On mousemove, if dragging, update the rectangle's position (here we simply recenter it under the cursor, using an offset might improve the feel) and redraw it. On mouseup, release the drag. The concept is straightforward: track a boolean and the shape position.

The code above uses `e.offsetX/Y` for simplicity (these give the mouse position relative to the target element, which is the canvas).

This pattern can be extended for multiple shapes (you’d check a list of shapes to see which was clicked, perhaps track a `dragTarget` reference). For complex interactive drawings, an easier approach might be to use a library or maintain a separate data structure for drawn objects.

### Keyboard Events

The canvas element can also receive keyboard input if it has focus, but usually you’d listen on the `window` or `document` for key events for games. You can capture `"keydown"` and `"keyup"` events:

```js
window.addEventListener("keydown", function(e) {
  if (e.key === "ArrowRight") player.x += 5;
  else if (e.key === "ArrowLeft") player.x -= 5;
});
```

In this pseudo-code, when the right or left arrow is pressed, we adjust a `player.x` position (assuming you have a player object). You would then redraw the canvas to reflect the new position. In an animation loop scenario, you might set some velocity and let the loop handle continuous movement until keyup.

For example, you could on keydown set `player.vx = 5` for right arrow and on keyup set it back to 0. The animation loop uses `player.vx` each frame to move the player.

**Note:** If you want the canvas to get keyboard events, it needs to be focusable/tabindex or you can handle global events. Often, games just use `document` events.

Combining keyboard and mouse interactions allows you to create rich interactive canvas apps (like drag-and-drop builders, paint programs, or games).

## 8. Advanced Graphics Techniques

Now let's cover some of the more advanced drawing techniques available on canvas, including curves, shadows, and compositing (blending).

### Bezier Curves

Canvas supports quadratic and cubic Bezier curves for smooth shapes:

- `ctx.quadraticCurveTo(cpx, cpy, x, y)` – Draws a quadratic Bezier curve from the current path point to (x,y) using (cpx, cpy) as the control point. Imagine the curve “bends” toward the control point. This needs one control point.
- `ctx.bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y)` – Draws a cubic Bezier with two control points (cp1 and cp2), allowing more complex shapes.

Remember, you must call `beginPath()` or have an open path, and usually you'll call `moveTo` first to set a start point.

**Example – Quadratic Curve (speech bubble tail):**

```js
ctx.beginPath();
ctx.moveTo(50, 20);
ctx.quadraticCurveTo(20, 100, 50, 180);  // control point (20,100), end point (50,180)
ctx.stroke();
```

This will draw a single curved line from (50,20) to (50,180) bulging toward (20,100). A quadratic Bezier is defined by start (implicitly the last moveTo point), one control, and end.

**Example – Cubic Bezier (heart shape piece):**

```js
ctx.beginPath();
ctx.moveTo(75, 40);
ctx.bezierCurveTo(75, 37, 70, 25, 50, 25);
ctx.bezierCurveTo(20, 25, 20, 62, 50, 62);
ctx.fill();
```

This is part of a heart shape example using two `bezierCurveTo` calls. Cubic Beziers use two control points each, giving you fine control over the curve’s entering and exiting angles. They are more complex but very powerful for designing shapes like hearts, cloud puffs, or any smooth curve shape.

It may take experimentation to understand how control points affect the curve. There are online tools to visualize Bezier curves that can help.

### Shadows

Canvas can draw shadows for any drawing (paths, text, images). Shadow properties on the context:

- `ctx.shadowColor = "rgba(0,0,0,0.5)"` – Color of the shadow ([HTML Canvas Shadows](https://www.w3schools.com/graphics/canvas_shadows.asp#:~:text=%2A%20%60shadowColor%60%20,shadows%20will%20be%20offset%20horizontally)).
- `ctx.shadowBlur = 10` – Blur level of the shadow (bigger number = more diffuse).
- `ctx.shadowOffsetX = dx`, `ctx.shadowOffsetY = dy` – How far to offset the shadow from the shape (in pixels).

Shadow is drawn when you fill or stroke shapes (or draw text/images) and applies to those drawing operations.

**Example – Text with Shadow:**

```js
ctx.shadowColor = "rgba(0,0,0,0.3)"; // semi-transparent black shadow
ctx.shadowBlur = 4;
ctx.shadowOffsetX = 5;
ctx.shadowOffsetY = 5;

ctx.font = "30px Georgia";
ctx.fillStyle = "orange";
ctx.fillText("Shadowed Text", 50, 100);
```

This will draw "Shadowed Text" in orange, with a slight blurred black shadow offset 5px right and down. Shadows can add depth but note: shadows affect performance, especially large blur values, so use them sparingly (the MDN optimization guide even suggests to avoid shadowBlur when possible for better speed).

### Composite Operations (Blending and Clipping)

The `globalCompositeOperation` property of the context defines how new drawing combines with what’s already on the canvas. Here are a few useful modes:

- `"source-over"`: Default. New drawing covers what was there (opaque by default, or alpha-blends if semi-transparent).
- `"destination-over"`: New drawing goes **behind** the existing content.
- `"source-atop"`: New drawing only shows up *on top of* existing content (it is clipped to the pixels that were already there).
- `"destination-atop"`: New drawing is put behind existing content but only where content already exists (other areas of new drawing are ignored).
- `"lighter"`: New colors are added to existing (like lighten/blend – overlapping colors get brighter combined) ([HTML Canvas Compositing](https://www.w3schools.com/graphics/canvas_compositing.asp#:~:text=match%20at%20L815%20Set%20,Then%20draw%20two%20overlapping%20rectangles)).
- `"multiply"`, `"screen"`, etc.: Many Photoshop-style blend modes (multiply darkens by combining, screen lightens, etc.).

**Example – globalCompositeOperation:**

```js
// Draw a blue and a red overlapping square normally (source-over)
ctx.globalCompositeOperation = "source-over";
ctx.fillStyle = "blue";
ctx.fillRect(20, 20, 60, 60);
ctx.fillStyle = "red";
ctx.fillRect(50, 50, 60, 60);  // overlaps part of blue
```

The area where they overlap will show the red (on top) normally in source-over mode (because we drew red second).

Now if we change mode:

```js
// Draw the same squares with 'lighter' mode
ctx.clearRect(0,0,canvas.width, canvas.height);
ctx.globalCompositeOperation = "lighter";
ctx.fillStyle = "blue";
ctx.fillRect(20, 20, 60, 60);
ctx.fillStyle = "red";
ctx.fillRect(50, 50, 60, 60);
```

In `"lighter"` mode, where blue and red overlap, you’ll see a lighter additive color (blue+red overlap may appear magenta or white-ish depending on intensity). Neither covers the other; instead their colors combine.

After drawing with a composite mode, you can set `globalCompositeOperation` back to `"source-over"` (or whatever mode you need next). The mode affects any draw calls while it’s set.

**Clipping Paths:** Another advanced feature is using a path as a clipping region via `ctx.clip()`. If you have a complex shape path and call `ctx.clip()`, further drawing is restricted to that shape (everything outside it is masked out). This can be used for things like drawing an image with a circular mask (draw a circle path, clip, then draw the image – the image only appears inside the circle). To remove a clipping region, you have to restore a saved state from before the clip (since clip is part of state).

Clipping is beyond the scope of a beginner tutorial but good to be aware of as you advance.

## 9. Basic Game Development with Canvas

By combining what we've learned — drawing, animation, and input handling — you can create simple 2D games. Canvas is well-suited for 2D games like platformers, puzzles, or classic arcade-style games.

Let's outline fundamental game development concepts on canvas:

### Game Loop

A game typically runs in a loop, updating the game state and rendering it many times per second. We can use `requestAnimationFrame` as our game loop timer (or a fixed `setInterval` if you prefer a fixed step, but `requestAnimationFrame` is simpler).

**Pseudo-code for a game loop:**

```js
function gameLoop() {
  updateGameState();    // e.g., move objects, handle collisions
  renderGame();         // draw everything using canvas operations
  requestAnimationFrame(gameLoop);
}
gameLoop(); // start the loop
```

In `updateGameState`, you'd update positions (based on velocities or user input), check for events (like collisions or scoring conditions). In `renderGame`, you'd clear the canvas and draw all game objects (background, player, enemies, etc.) in their new positions.

### Moving a Character with Keyboard

If you have a player square that you want to move with arrow keys:

```js
let player = { x: 50, y: 50, width: 20, height: 20, speed: 5 };
let keys = {};
window.addEventListener("keydown", e => { keys[e.key] = true; });
window.addEventListener("keyup", e => { keys[e.key] = false; });

function updateGameState() {
  // Update player velocity based on keys pressed
  if (keys["ArrowRight"]) player.x += player.speed;
  if (keys["ArrowLeft"])  player.x -= player.speed;
  if (keys["ArrowDown"])  player.y += player.speed;
  if (keys["ArrowUp"])    player.y -= player.speed;
  
  // Keep player within bounds
  if (player.x < 0) player.x = 0;
  if (player.x + player.width > canvas.width) player.x = canvas.width - player.width;
  // similarly for y...
}

function renderGame() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "green";
  ctx.fillRect(player.x, player.y, player.width, player.height);
}
```

Here we use an object `keys` to track which keys are pressed (on keydown we set the key name true, on keyup set false). In the game loop, we adjust the player's position according to which arrow keys are currently pressed. We also ensure the player doesn't move out of the canvas.

### Collision Detection

Detecting collisions (e.g., player picks up an item or hits an enemy) is usually done in the update step by checking overlapping areas.

For simple rectangular collision (Axis-Aligned Bounding Box collision):

```js
function isColliding(rect1, rect2) {
  return !(rect1.x > rect2.x + rect2.width  || 
           rect1.x + rect1.width < rect2.x  || 
           rect1.y > rect2.y + rect2.height || 
           rect1.y + rect1.height < rect2.y);
}
```

This returns true if two rectangles overlap. It’s basically the inverse of checking that one is completely to the left/right or above/below the other.

If you have a player and an enemy:

```js
if (isColliding(player, enemy)) {
  // handle collision, e.g., end game or reduce health
}
```

For circular objects, you'd check distance between centers <= sum of radii for collision.

### Example – Simple Avoidance Game

Let's say a player square must avoid an obstacle square that moves:

```js
let obstacle = { x: 300, y: 0, width: 20, height: 20, speedY: 2 };

function updateGameState() {
  // Move obstacle down
  obstacle.y += obstacle.speedY;
  if (obstacle.y > canvas.height) {
    obstacle.y = -obstacle.height; // reset to top once it goes off bottom
  }
  // Move player with keys (as above)
  // ...
  // Collision
  if (isColliding(player, obstacle)) {
    console.log("Game Over");
    // Stop the game loop or reset game
    cancelAnimationFrame(gameId); // (you'd need to store the requestAnimationFrame id to cancel)
  }
}

function renderGame() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // draw player
  ctx.fillStyle = "green";
  ctx.fillRect(player.x, player.y, player.width, player.height);
  // draw obstacle
  ctx.fillStyle = "red";
  ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
}
```

This is a rudimentary game where a red obstacle falls from the top repeatedly and the player must dodge it. If the green player hits the red obstacle, we log "Game Over" and stop the loop. (In a real game you might display a message or restart.)

### Game Loop Integration

Combine `updateGameState` and `renderGame` in a loop:

```js
function gameLoop() {
  updateGameState();
  renderGame();
  gameId = requestAnimationFrame(gameLoop); // save ID if we want to cancel later
}
gameLoop();
```

Now you have a continuously updating game. This pattern can be expanded with multiple enemies, scoring (increment a score variable each frame or when something happens), and other game logic.

## 10. Performance Optimization Tips

Canvas can handle a lot, but to keep animations and games running smoothly, consider these optimization tips:

- **Redraw only what you need:** If only a small part of the canvas changes, you don't have to clear and redraw everything. You can use small `clearRect` and redraw only certain objects. However, in many games everything moves, so full redraw is fine. For static backgrounds, consider drawing the background once and then only drawing moving elements on top.

- **Avoid unnecessary state changes:** Minimize setting properties over and over. For example, if you are drawing many shapes in the same color, set `fillStyle` once before the loop rather than inside the loop for each shape.

- **Use off-screen canvas for complex drawing:** You can create a separate canvas (not added to DOM) to pre-render complex graphics or large images, then use `drawImage` to blit it onto the visible canvas. For example, if your game has a static background with many details, draw it to an offscreen canvas once, then each frame just draw that offscreen canvas onto the visible one – this is usually faster than re-drawing the complex background every frame.

  ```js
  const bgCanvas = document.createElement('canvas');
  bgCanvas.width = canvas.width;
  bgCanvas.height = canvas.height;
  const bgCtx = bgCanvas.getContext('2d');
  // draw heavy background on bgCtx...
  // later in animation loop:
  ctx.drawImage(bgCanvas, 0, 0);
  // then draw players, enemies, etc. on top
  ```

  This way, drawing the background is just a fast blit of a cached image.

- **Use integer coordinates when possible:** Drawing at exact pixel positions avoids anti-aliasing blurs. If you can, align shapes on whole pixels to render a bit faster and sharper ([Optimizing canvas - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Optimizing_canvas#:~:text=Avoid%20floating,integers%20instead)) (especially for pixel-art style games).

- **Limit shadow and text usage:** Shadows (especially with blur) and drawing text are relatively slower operations. If you need a lot of text (like a scoreboard), update it only when it changes, not every frame. Avoid heavy shadows in animations or apply them to an offscreen canvas and reuse the result.

- **Layered canvases:** Sometimes using multiple canvas elements layered in HTML can help. For example, one canvas for static background, one for main game, one for UI. This can simplify redraw logic (you only clear the canvas that needs updates). It won't boost rendering performance per se, but can help organize complex scenes (e.g., a HUD that doesn't need clearing when the game scene updates).

- **Clipping and Path2D:** If you reuse a complex path often, consider using `Path2D` objects which let you store a path and reuse it without recalculating it each time. This can speed up rendering of repetitive shapes.

- **Web Workers and OffscreenCanvas:** For very heavy graphics computations, Canvas can be used off the main thread using `OffscreenCanvas` (in browsers that support it). This is an advanced topic where you can actually move rendering to a web worker thread.

Most simple games and animations will run fine with the straightforward approach as long as you don't do something extremely heavy each frame. Always profile if you run into performance issues: maybe the bottleneck is not the canvas drawing but your own game logic (e.g., an overly complex collision check). Use the tips above to optimize the drawing part.

---

**Conclusion:** You should now have a good grasp of the HTML5 Canvas API, from the basics of drawing shapes and text, to handling images and animations, to building interactive content like games. The Canvas API is quite extensive (there are more features and quirks to explore), but with practice you can create a wide range of graphics-oriented applications. Be sure to experiment with the code examples above, and happy drawing on the canvas!