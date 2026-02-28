{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c4c4de0f-9a9c-4d65-8626-e80a47b826a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING:absl:Compiled the loaded model, but the compiled metrics have yet to be built. `model.compile_metrics` will be empty until you train or evaluate the model.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">Model: \"functional\"</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1mModel: \"functional\"\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\">┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓\n",
       "┃<span style=\"font-weight: bold\"> Layer (type)                    </span>┃<span style=\"font-weight: bold\"> Output Shape           </span>┃<span style=\"font-weight: bold\">       Param # </span>┃\n",
       "┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩\n",
       "│ input_layer (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">InputLayer</span>)        │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">224</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">224</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">3</span>)    │             <span style=\"color: #00af00; text-decoration-color: #00af00\">0</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block1_conv1 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">224</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">224</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">64</span>)   │         <span style=\"color: #00af00; text-decoration-color: #00af00\">1,792</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block1_conv2 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">224</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">224</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">64</span>)   │        <span style=\"color: #00af00; text-decoration-color: #00af00\">36,928</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block1_pool (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">MaxPooling2D</span>)      │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">112</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">112</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">64</span>)   │             <span style=\"color: #00af00; text-decoration-color: #00af00\">0</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block2_conv1 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">112</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">112</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">128</span>)  │        <span style=\"color: #00af00; text-decoration-color: #00af00\">73,856</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block2_conv2 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">112</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">112</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">128</span>)  │       <span style=\"color: #00af00; text-decoration-color: #00af00\">147,584</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block2_pool (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">MaxPooling2D</span>)      │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">56</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">56</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">128</span>)    │             <span style=\"color: #00af00; text-decoration-color: #00af00\">0</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block3_conv1 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">56</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">56</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">256</span>)    │       <span style=\"color: #00af00; text-decoration-color: #00af00\">295,168</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block3_conv2 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">56</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">56</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">256</span>)    │       <span style=\"color: #00af00; text-decoration-color: #00af00\">590,080</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block3_conv3 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">56</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">56</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">256</span>)    │       <span style=\"color: #00af00; text-decoration-color: #00af00\">590,080</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block3_conv4 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">56</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">56</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">256</span>)    │       <span style=\"color: #00af00; text-decoration-color: #00af00\">590,080</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block3_pool (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">MaxPooling2D</span>)      │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">28</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">28</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">256</span>)    │             <span style=\"color: #00af00; text-decoration-color: #00af00\">0</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block4_conv1 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">28</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">28</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">512</span>)    │     <span style=\"color: #00af00; text-decoration-color: #00af00\">1,180,160</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block4_conv2 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">28</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">28</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">512</span>)    │     <span style=\"color: #00af00; text-decoration-color: #00af00\">2,359,808</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block4_conv3 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">28</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">28</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">512</span>)    │     <span style=\"color: #00af00; text-decoration-color: #00af00\">2,359,808</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block4_conv4 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">28</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">28</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">512</span>)    │     <span style=\"color: #00af00; text-decoration-color: #00af00\">2,359,808</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block4_pool (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">MaxPooling2D</span>)      │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">14</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">14</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">512</span>)    │             <span style=\"color: #00af00; text-decoration-color: #00af00\">0</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block5_conv1 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">14</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">14</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">512</span>)    │     <span style=\"color: #00af00; text-decoration-color: #00af00\">2,359,808</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block5_conv2 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">14</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">14</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">512</span>)    │     <span style=\"color: #00af00; text-decoration-color: #00af00\">2,359,808</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block5_conv3 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">14</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">14</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">512</span>)    │     <span style=\"color: #00af00; text-decoration-color: #00af00\">2,359,808</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block5_conv4 (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Conv2D</span>)           │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">14</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">14</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">512</span>)    │     <span style=\"color: #00af00; text-decoration-color: #00af00\">2,359,808</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block5_pool (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">MaxPooling2D</span>)      │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">7</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">7</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">512</span>)      │             <span style=\"color: #00af00; text-decoration-color: #00af00\">0</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ flatten (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Flatten</span>)               │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">25088</span>)          │             <span style=\"color: #00af00; text-decoration-color: #00af00\">0</span> │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ dense (<span style=\"color: #0087ff; text-decoration-color: #0087ff\">Dense</span>)                   │ (<span style=\"color: #00d7ff; text-decoration-color: #00d7ff\">None</span>, <span style=\"color: #00af00; text-decoration-color: #00af00\">20</span>)             │       <span style=\"color: #00af00; text-decoration-color: #00af00\">501,780</span> │\n",
       "└─────────────────────────────────┴────────────────────────┴───────────────┘\n",
       "</pre>\n"
      ],
      "text/plain": [
       "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓\n",
       "┃\u001b[1m \u001b[0m\u001b[1mLayer (type)                   \u001b[0m\u001b[1m \u001b[0m┃\u001b[1m \u001b[0m\u001b[1mOutput Shape          \u001b[0m\u001b[1m \u001b[0m┃\u001b[1m \u001b[0m\u001b[1m      Param #\u001b[0m\u001b[1m \u001b[0m┃\n",
       "┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩\n",
       "│ input_layer (\u001b[38;5;33mInputLayer\u001b[0m)        │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m224\u001b[0m, \u001b[38;5;34m224\u001b[0m, \u001b[38;5;34m3\u001b[0m)    │             \u001b[38;5;34m0\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block1_conv1 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m224\u001b[0m, \u001b[38;5;34m224\u001b[0m, \u001b[38;5;34m64\u001b[0m)   │         \u001b[38;5;34m1,792\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block1_conv2 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m224\u001b[0m, \u001b[38;5;34m224\u001b[0m, \u001b[38;5;34m64\u001b[0m)   │        \u001b[38;5;34m36,928\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block1_pool (\u001b[38;5;33mMaxPooling2D\u001b[0m)      │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m112\u001b[0m, \u001b[38;5;34m112\u001b[0m, \u001b[38;5;34m64\u001b[0m)   │             \u001b[38;5;34m0\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block2_conv1 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m112\u001b[0m, \u001b[38;5;34m112\u001b[0m, \u001b[38;5;34m128\u001b[0m)  │        \u001b[38;5;34m73,856\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block2_conv2 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m112\u001b[0m, \u001b[38;5;34m112\u001b[0m, \u001b[38;5;34m128\u001b[0m)  │       \u001b[38;5;34m147,584\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block2_pool (\u001b[38;5;33mMaxPooling2D\u001b[0m)      │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m56\u001b[0m, \u001b[38;5;34m56\u001b[0m, \u001b[38;5;34m128\u001b[0m)    │             \u001b[38;5;34m0\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block3_conv1 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m56\u001b[0m, \u001b[38;5;34m56\u001b[0m, \u001b[38;5;34m256\u001b[0m)    │       \u001b[38;5;34m295,168\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block3_conv2 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m56\u001b[0m, \u001b[38;5;34m56\u001b[0m, \u001b[38;5;34m256\u001b[0m)    │       \u001b[38;5;34m590,080\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block3_conv3 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m56\u001b[0m, \u001b[38;5;34m56\u001b[0m, \u001b[38;5;34m256\u001b[0m)    │       \u001b[38;5;34m590,080\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block3_conv4 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m56\u001b[0m, \u001b[38;5;34m56\u001b[0m, \u001b[38;5;34m256\u001b[0m)    │       \u001b[38;5;34m590,080\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block3_pool (\u001b[38;5;33mMaxPooling2D\u001b[0m)      │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m28\u001b[0m, \u001b[38;5;34m28\u001b[0m, \u001b[38;5;34m256\u001b[0m)    │             \u001b[38;5;34m0\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block4_conv1 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m28\u001b[0m, \u001b[38;5;34m28\u001b[0m, \u001b[38;5;34m512\u001b[0m)    │     \u001b[38;5;34m1,180,160\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block4_conv2 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m28\u001b[0m, \u001b[38;5;34m28\u001b[0m, \u001b[38;5;34m512\u001b[0m)    │     \u001b[38;5;34m2,359,808\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block4_conv3 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m28\u001b[0m, \u001b[38;5;34m28\u001b[0m, \u001b[38;5;34m512\u001b[0m)    │     \u001b[38;5;34m2,359,808\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block4_conv4 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m28\u001b[0m, \u001b[38;5;34m28\u001b[0m, \u001b[38;5;34m512\u001b[0m)    │     \u001b[38;5;34m2,359,808\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block4_pool (\u001b[38;5;33mMaxPooling2D\u001b[0m)      │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m14\u001b[0m, \u001b[38;5;34m14\u001b[0m, \u001b[38;5;34m512\u001b[0m)    │             \u001b[38;5;34m0\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block5_conv1 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m14\u001b[0m, \u001b[38;5;34m14\u001b[0m, \u001b[38;5;34m512\u001b[0m)    │     \u001b[38;5;34m2,359,808\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block5_conv2 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m14\u001b[0m, \u001b[38;5;34m14\u001b[0m, \u001b[38;5;34m512\u001b[0m)    │     \u001b[38;5;34m2,359,808\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block5_conv3 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m14\u001b[0m, \u001b[38;5;34m14\u001b[0m, \u001b[38;5;34m512\u001b[0m)    │     \u001b[38;5;34m2,359,808\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block5_conv4 (\u001b[38;5;33mConv2D\u001b[0m)           │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m14\u001b[0m, \u001b[38;5;34m14\u001b[0m, \u001b[38;5;34m512\u001b[0m)    │     \u001b[38;5;34m2,359,808\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ block5_pool (\u001b[38;5;33mMaxPooling2D\u001b[0m)      │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m7\u001b[0m, \u001b[38;5;34m7\u001b[0m, \u001b[38;5;34m512\u001b[0m)      │             \u001b[38;5;34m0\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ flatten (\u001b[38;5;33mFlatten\u001b[0m)               │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m25088\u001b[0m)          │             \u001b[38;5;34m0\u001b[0m │\n",
       "├─────────────────────────────────┼────────────────────────┼───────────────┤\n",
       "│ dense (\u001b[38;5;33mDense\u001b[0m)                   │ (\u001b[38;5;45mNone\u001b[0m, \u001b[38;5;34m20\u001b[0m)             │       \u001b[38;5;34m501,780\u001b[0m │\n",
       "└─────────────────────────────────┴────────────────────────┴───────────────┘\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\"> Total params: </span><span style=\"color: #00af00; text-decoration-color: #00af00\">20,526,166</span> (78.30 MB)\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1m Total params: \u001b[0m\u001b[38;5;34m20,526,166\u001b[0m (78.30 MB)\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\"> Trainable params: </span><span style=\"color: #00af00; text-decoration-color: #00af00\">501,780</span> (1.91 MB)\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1m Trainable params: \u001b[0m\u001b[38;5;34m501,780\u001b[0m (1.91 MB)\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\"> Non-trainable params: </span><span style=\"color: #00af00; text-decoration-color: #00af00\">20,024,384</span> (76.39 MB)\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1m Non-trainable params: \u001b[0m\u001b[38;5;34m20,024,384\u001b[0m (76.39 MB)\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\"> Optimizer params: </span><span style=\"color: #00af00; text-decoration-color: #00af00\">2</span> (12.00 B)\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1m Optimizer params: \u001b[0m\u001b[38;5;34m2\u001b[0m (12.00 B)\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from tensorflow.keras.models import load_model\n",
    "\n",
    "model = load_model(\"dog_breed_model.h5\")\n",
    "model.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3df29698-e71a-4a9f-ae2b-db99d8b6693a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (apsche_tf)",
   "language": "python",
   "name": "apsche_tf"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
