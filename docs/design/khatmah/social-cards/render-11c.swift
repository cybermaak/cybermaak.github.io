// Deterministic social-card composition; no generated or redrawn app UI.
import AppKit
import Foundation

let here = URL(fileURLWithPath: #filePath).deletingLastPathComponent()
let root = here.deletingLastPathComponent().deletingLastPathComponent().deletingLastPathComponent().deletingLastPathComponent()
let assets = root.appendingPathComponent("public/khatmah/assets")
let output = CommandLine.arguments.count > 1 ? URL(fileURLWithPath: CommandLine.arguments[1]) : here
try FileManager.default.createDirectory(at: output, withIntermediateDirectories: true)
let W: CGFloat = 1200, H: CGFloat = 630
func color(_ hex: String) -> NSColor {
    let n = UInt32(hex, radix: 16)!
    return NSColor(srgbRed: CGFloat((n >> 16) & 255)/255, green: CGFloat((n >> 8) & 255)/255, blue: CGFloat(n & 255)/255, alpha: 1)
}
func fill(_ hex: String, _ rect: NSRect) { color(hex).setFill(); rect.fill() }
func line(_ hex: String, _ rect: NSRect) { fill(hex,rect) }
func image(_ file: String, _ rect: NSRect) {
    guard let image = NSImage(contentsOf: assets.appendingPathComponent(file)) else { fatalError("Missing public asset: \(file)") }
    image.draw(in: rect, from: .zero, operation: .sourceOver, fraction: 1, respectFlipped: true, hints: [.interpolation:NSImageInterpolation.high])
}
func icon(_ rect: NSRect) {
    NSGraphicsContext.saveGraphicsState()
    NSBezierPath(roundedRect:rect,xRadius:rect.width*0.22,yRadius:rect.height*0.22).addClip()
    image("icon.jpg",rect)
    NSGraphicsContext.restoreGraphicsState()
}
func text(_ value: String, _ rect: NSRect, size: CGFloat, hex: String, ar: Bool = false, serif: Bool = false, centered: Bool = false) {
    let name = ar ? "GeezaPro" : (serif ? "Georgia" : "HelveticaNeue")
    guard let font = NSFont(name: name, size: size) else { fatalError("Required font unavailable: \(name)") }
    let p = NSMutableParagraphStyle()
    p.alignment = centered ? .center : (ar ? .right : .left)
    p.baseWritingDirection = ar ? .rightToLeft : .leftToRight
    p.lineBreakMode = .byWordWrapping
    p.lineSpacing = ar ? 8 : 5
    let a = NSAttributedString(string:value, attributes:[.font:font,.foregroundColor:color(hex),.paragraphStyle:p])
    let bounds = a.boundingRect(with: NSSize(width:rect.width,height:2000),options:[.usesLineFragmentOrigin,.usesFontLeading])
    precondition(bounds.height <= rect.height + 1, "Text does not fit: \(value), \(bounds.height) > \(rect.height)")
    a.draw(with:rect,options:[.usesLineFragmentOrigin,.usesFontLeading])
}
func phone(_ file: String, x: CGFloat, y: CGFloat, h: CGFloat) {
    let w = h * 1470 / 3000
    let screen = NSRect(x:x+w*75/1470,y:y+h*66/3000,width:w*1320/1470,height:h*2868/3000)
    NSGraphicsContext.saveGraphicsState()
    NSBezierPath(roundedRect:screen,xRadius:w*0.09,yRadius:w*0.09).addClip()
    image(file,screen)
    NSGraphicsContext.restoreGraphicsState()
    image("iphone-18-pro-max-black-portrait.png",NSRect(x:x,y:y,width:w,height:h))
}
func stroke(_ path: NSBezierPath, hex: String = "a1761f", alpha: CGFloat = 0.18, width: CGFloat = 1) {
    color(hex).withAlphaComponent(alpha).setStroke()
    path.lineWidth = width
    path.stroke()
}
func star(x: CGFloat, y: CGFloat, radius: CGFloat, alpha: CGFloat) {
    let p = NSBezierPath()
    for i in 0..<16 {
        let angle = CGFloat(i) * .pi / 8 - .pi / 2
        let r = i % 2 == 0 ? radius : radius * 0.54
        let point = NSPoint(x:x + cos(angle)*r, y:y + sin(angle)*r)
        if i == 0 { p.move(to:point) } else { p.line(to:point) }
    }
    p.close(); stroke(p,alpha:alpha,width:0.8)
}
func paper() {
    fill("fffdf8",NSRect(x:0,y:0,width:W,height:H))
    // Fixed low-contrast fibers, not random texture or image synthesis.
    for row in 0..<90 { for col in 0..<150 {
        let n = (row * 73 + col * 37) % 13
        if n < 3 {
            color("b19b73").withAlphaComponent(0.025).setFill()
            NSRect(x:CGFloat(col*8+n),y:CGFloat(row*7),width:CGFloat(n+1),height:0.5).fill()
        }
    }}
}
func ornament(center: CGFloat, y: CGFloat) {
    let p=NSBezierPath();p.move(to:NSPoint(x:center-80,y:y));p.line(to:NSPoint(x:center-15,y:y))
    p.move(to:NSPoint(x:center+15,y:y));p.line(to:NSPoint(x:center+80,y:y))
    stroke(p,alpha:0.32)
    star(x:center,y:y,radius:5,alpha:0.42)
}
// Raw screenshot panels, not Apple hardware mockups; source pixels stay intact.
func panel(_ file: String, cx: CGFloat, cy: CGFloat, width: CGFloat, angle: CGFloat = 0, alpha: CGFloat = 1, shadow: Bool = true) {
    let source = NSImage(contentsOf:assets.appendingPathComponent(file))!
    let height = width * source.size.height / source.size.width
    NSGraphicsContext.saveGraphicsState()
    let ctx=NSGraphicsContext.current!.cgContext
    ctx.translateBy(x:cx,y:cy);ctx.rotate(by:angle * .pi / 180)
    let rect=NSRect(x:-width/2,y:-height/2,width:width,height:height)
    let shape=NSBezierPath(roundedRect:rect,xRadius:22,yRadius:22)
    if shadow {
        NSGraphicsContext.saveGraphicsState()
        let drop=NSShadow();drop.shadowColor=color("49351b").withAlphaComponent(0.17);drop.shadowBlurRadius=28;drop.shadowOffset=NSSize(width:0,height:-10);drop.set()
        color("fffdf8").setFill();shape.fill()
        NSGraphicsContext.restoreGraphicsState()
    }
    shape.addClip()
    source.draw(in:rect,from:.zero,operation:.sourceOver,fraction:alpha,respectFlipped:true,hints:[.interpolation:NSImageInterpolation.high])
    NSGraphicsContext.restoreGraphicsState()
}
func brand(ar: Bool, center: CGFloat, iconY: CGFloat, iconSize: CGFloat, nameY: CGFloat, nameSize: CGFloat, width: CGFloat = 570) {
    icon(NSRect(x:center-iconSize/2,y:iconY,width:iconSize,height:iconSize))
    text(ar ? "ختمة" : "Khatmah",NSRect(x:center-width/2,y:nameY,width:width,height:170),size:ar ? nameSize+8 : nameSize,hex:"241a0a",ar:ar,serif:true,centered:true)
}
// Revision 11C: stronger framed background, localized official download badge.
func render(_ ar: Bool) -> NSImage {
    NSImage(size:NSSize(width:W,height:H),flipped:true) { _ in
        paper()
        let ctx=NSGraphicsContext.current!.cgContext
        NSGraphicsContext.saveGraphicsState()
        ctx.translateBy(x:ar ? 240 : 960,y:650)
        ctx.rotate(by:(ar ? 9 : -9) * .pi / 180)
        ctx.setAlpha(0.82)
        ctx.beginTransparencyLayer(auxiliaryInfo:nil)
        phone(ar ? "page-ar.png" : "page.png",x:-294,y:-600,h:1200)
        ctx.endTransparencyLayer()
        NSGraphicsContext.restoreGraphicsState()
        let gradient=NSGradient(colors:[color("fffdf8"),color("fffdf8").withAlphaComponent(0.65),color("fffdf8").withAlphaComponent(0)])!
        gradient.draw(in:NSRect(x:0,y:0,width:1200,height:630),angle:ar ? 180 : 0)
        let center:CGFloat=ar ? 885 : 315
        if ar {
            // The icon's own Arabic lettering is the sole product title.
            icon(NSRect(x:center-160,y:106,width:320,height:320))
        } else {
            brand(ar:false,center:center,iconY:106,iconSize:176,nameY:309,nameSize:92)
        }
        let badge=ar ? "app-store-badge-ar.svg" : "app-store-badge.svg"
        image(badge,NSRect(x:center-110,y:474,width:220,height:220*40/119.66407))
        return true
    }
}
func save(_ image: NSImage, _ name: String) throws {
    guard let cg=image.cgImage(forProposedRect:nil,context:nil,hints:nil) else { fatalError("Render failed") }
    let rep=NSBitmapImageRep(cgImage:cg)
    guard let data=rep.representation(using:.png,properties:[:]) else { fatalError("PNG failed") }
    try data.write(to:output.appendingPathComponent(name))
}
for ar in [false,true] { try save(render(ar), "11c-" + (ar ? "ar" : "en") + ".png") }
let pair=NSImage(size:NSSize(width:1200,height:1284),flipped:true) { _ in
    fill("e2d8c4",NSRect(x:0,y:0,width:1200,height:1284))
    render(false).draw(in:NSRect(x:0,y:0,width:1200,height:630),from:.zero,operation:.sourceOver,fraction:1,respectFlipped:true,hints:nil)
    render(true).draw(in:NSRect(x:0,y:654,width:1200,height:630),from:.zero,operation:.sourceOver,fraction:1,respectFlipped:true,hints:nil)
    return true
}
try save(pair,"11c-pair.png")
print("Rendered 11C: English, Arabic, comparison")
