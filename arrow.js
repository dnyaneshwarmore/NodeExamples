var cat = {
    lives: 9,
    jumps: function a ()  {
      this.lives--;
    }
  }

  cat.jumps()
  console.log(cat)