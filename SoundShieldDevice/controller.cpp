/* 
Hardware list:
- Raspberry Pico
- CJMCU-1334 DAC
- Fosi Audio BT20A amplifier
- MAX98357 microphone, input
- DAEX25Q-4 exciter, output
*/

#include "pico/stdlib.h"
#include "hardware/i2s.h"
#include "hardware/i2c.h"
#include "hardware/gpio.h"
#include "MAX98357.h"

// Constants
const uint LED_PIN = 25;
const uint I2C_SDA_PIN = 4;
const uint I2C_SCL_PIN = 5;
const uint I2S_DATA_PIN = 2;
const uint I2S_CLOCK_PIN_BASE = 6;

// DAC and Microphone objects
MAX98357 microphone(I2S_DATA_PIN, I2S_CLOCK_PIN_BASE);

// Function to initialize I2C communication with the CJMCU-1334 DAC
void init_dac() {
  i2c_init(i2c_default, 100 * 1000);
  gpio_set_function(I2C_SDA_PIN, GPIO_FUNC_I2C);
  gpio_set_function(I2C_SCL_PIN, GPIO_FUNC_I2C);
  gpio_pull_up(I2C_SDA_PIN);
  gpio_pull_up(I2C_SCL_PIN);
  // init DAC
}

// Function to write data to the DAC
void write_dac_data(int16_t data) {
  // write data to DAC
}

// Function to process the audio samples and generate the anti-sound signal
int16_t process_audio(int16_t sample) {
  // adaptive-filtering
  return -sample;
}

int main() {
  stdio_init_all();
  gpio_init(LED_PIN);
  gpio_set_dir(LED_PIN, GPIO_OUT);

  init_dac();
  microphone.begin();

  while (true) {
    int16_t audio_sample = microphone.read_audio_sample();
    int16_t anti_sound_sample = process_audio(audio_sample);
    write_dac_data(anti_sound_sample);
  }
}
