const fs = require('fs');
const path = require('path');
const _ = require('underscore');

// Return only base file name without dir
function getRecentClip(dir) {
  var files = fs.readdirSync(dir);

  // use underscore for max()
  return _.max(files, function (f) {
    var fullpath = path.join(dir, f);

    // ctime = creation time is used
    // replace with mtime for modification time
    return fs.statSync(fullpath).ctime;
  });
}