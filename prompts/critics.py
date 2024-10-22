# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


MAGAZINE_EDITOR_PROMPT = """

You're a friendly visual magazine editor who loves AI generated images with Imagen 3, Google's latest image generation model whose quality exceeds all leading external competitors in aesthetics, defect-free, and text image alignment. You are always friendly and positive and not shy to provide critiques with delightfully cheeky, clever streak. You've been presented with these images for your thoughts.

The prompt used by the author to create these images was: "{}"
    
Create a few sentence critique and commentary (3-4 sentences) complimenting each these images individually and together, paying special attention to quality of each image such calling out anything you notice in these following areas:
* Alignment with prompt - how well each image mached the given text prompt
* Photorealism - how closely the image resembles the type of image requested to be generated
* Detail - the level of detail and overall clarity
* Defects - any visible artifacts, distortions, or errors

Include aesthetic qualities (come up with a score). Include commentary on color, tone, subject, lighting, and composition. You may address the author as "you."

"""


REWRITER_PROMPT = """Write a prompt for a text-to-image model following the style of the examples of prompts, and then I will give you a prompt that I want you to rewrite.

Examples of prompts:

A close-up of a sleek Siamese cat perched regally, in front of a deep purple background, in a high-resolution photograph with fine details and color grading.
A luxurious bathroom with a predominantly light and neutral color palette accented by dark wood and gold.  Walls and Flooring: The walls feature light beige, square tiles, creating a clean, minimalist backdrop. A dark marble panel runs horizontally along the lower portion of the wall, providing a stylish contrast. The floor is large-format, light grey marble-like tiles with subtle veining.  Bathtub: A freestanding, white bathtub with a gold-colored base sits centrally in the room. It's rectangular with softly rounded corners and a modern, sleek design. A dark grey towel is draped over the side.  Sinks and Vanity: A double sink vanity sits against the wall. The sinks are rectangular and white, under-mounted in a rich dark wood vanity with three drawers. Gold-colored faucets are mounted on the vanity's backsplash.  Lighting: A three-light pendant fixture hangs above the bathtub. The pendant has a black frame and gold-colored spherical shades.  Mirrors: Two mirrors hang on the wall above the sinks. One is a large, rectangular mirror with a thin gold frame; the other is a smaller, rectangular vertical mirror. A third, slender, vertical mirror is mounted on the wall beside the other mirrors.  Accessories and Decor: A simple, dark wood shelving unit with black shelves holds towels and decorative objects (like a ceramic vase) on the wall. A long, low bench with a wooden frame and light colored cushion sits near the window.  Window: Large windows provide a city view, showing the New York City skyline, including the Empire State Building.  Overall Style: The bathroom's style is contemporary and luxurious, emphasizing clean lines, high-quality materials, and a sophisticated color scheme. The combination of warm wood tones and cool, neutral colors creates a balanced and serene atmosphere.
Overall Style: Minimalist, modern, with a spa-like feel. The color palette is neutral and calming, focusing on beige/taupe tones and natural wood. The design incorporates clean lines and simple shapes.
Floor and Walls: Light beige/taupe large-format tiles cover the floor and walls, creating a seamless look. The grout lines are minimal and consistent in color.
Vanity: A simple, rectangular vanity unit with a light-colored countertop sits below a wall-mounted mirror. The mirror is framed and features integrated lighting. A rectangular undermount sink is positioned centrally on the countertop.
Toilet: A wall-hung toilet is mounted on the left side of the room, maintaining the clean, uncluttered look.
Shower: A walk-in shower is separated from the rest of the bathroom by a black metal frame. The shower floor is lined with wooden slats (light brown, likely oak or similar), matching the wooden slat wall behind the vanity. A rainfall shower head is mounted on the wall.
Accessories: Minimalist accessories are used. These include a small soap dispenser, a towel rack (with a dark gray/brown towel), and a small storage container (likely for toiletries). A small branch with leaves adds a natural touch near the sink. A white storage unit, possibly for linens, sits on the floor near the toilet.
Lighting: The mirror's integrated lighting is the primary light source, providing soft illumination to the vanity area. Ambient lighting is implied but not directly shown.
Specific details for AI replication:
Tile texture: Specify a matte or slightly textured tile to mimic natural stone. The AI needs to understand the subtle variations in tone and texture that would appear on a real tile.
Wood type and finish: Specify the wood type (oak is likely) and the finish (possibly a matte or natural finish, not highly polished).
Metal finishes: Indicate that the metal fixtures (faucet, shower head, frame) have a brushed nickel or chrome finish.
Perspective: The image is an overhead perspective. Be sure to tell the AI model this is a bird's eye view.
Scale: You might need to specify the dimensions of the room and major fixtures for accuracy.
Flat vector illustration of "Breathe deep" hand-lettering with floral and leaf decorations. Bright colors, simple lines, and a cute, minimalist design on a white background.
Long exposure photograph of rocks and sea, long shot of cloudy skies, golden hour at the rocky shore with reflections in the water. High resolution.
Three women stand together laughing, with one woman slightly out of focus in the foreground. The sun is setting behind the women, creating a lens flare and a warm glow that highlights their hair and creates a bokeh effect in the background. The photography style is candid and captures a genuine moment of connection and happiness between friends. The warm light of golden hour lends a nostalgic and intimate feel to the image.
A group of five friends are standing together outdoors with tall gray mountains in the background. One woman is wearing a black and white striped top and is laughing with her hand on her mouth. The man next to her is wearing a blue and green plaid shirt, khaki shorts, and a camera around his neck, he is laughing and has his arm around another man who is bent over laughing wearing a gray shirt and black pants with a camera around his neck. Behind them, a blonde woman with sunglasses on her head and wearing a beige top and red backpack is laughing and pushing the man in the gray shirt.
An elderly woman with gray hair is sitting on a park bench next to a medium-sized brown and white dog, with the sun setting behind them, creating a warm orange glow and lens flare. She is wearing a straw sun hat and a pink patterned jacket and has a peaceful expression as she looks off into the distance.
A woman with blonde hair wearing sunglasses stands amidst a dazzling display of golden bokeh lights. Strands of lights and crystals partially obscure her face, and her sunglasses reflect the lights. The light is low and warm creating a festive atmosphere and the bright reflections in her glasses and the bokeh. This is a lifestyle portrait with elements of fashion photography.
A closeup of an intricate, dew-covered flower in the rain. The focus is on the delicate petals and water droplets, capturing their soft pastel colors against a dark blue background. Shot from eye level using natural light to highlight the floral texture and dew's glistening effect. This image conveys the serene beauty found within nature's miniature worlds in the style of realist details
A closeup of a pair of worn hands, wrinkled and weathered, gently cupping a freshly baked loaf of bread. The focus is on the contrast between the rough hands and the soft dough, with flour dusting the scene. Warm light creates a sense of nourishment and tradition in the style of realistic details
A Dalmatian dog in front of a pink background in a full body dynamic pose shot with high resolution photography and fine details isolated on a plain stock photo with color grading in the style of a hyper realistic style
A massive spaceship floating above an industrial city, with the lights of thousands of buildings glowing in the dusk. The atmosphere is dark and mysterious, in the cyberpunk style, and cinematic
An architectural photograph of an interior space made from interwoven, organic forms and structures inspired in the style of coral reefs and patterned textures. The scene is bathed in the warm glow of natural light, creating intricate shadows that accentuate the fluidity and harmony between the different elements within the design

Prompt to rewrite:

'{}'

Don’t generate images, provide only the rewritten prompt.
"""